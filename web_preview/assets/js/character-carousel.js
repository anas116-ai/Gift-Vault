/**
 * ThreeUI <CharacterCarousel /> - Filmstrip Variant (character-filmstrip)
 * Source revision: SHA-256 4c98939e0e2b (canonical-source character-filmstrip.html)
 * Preserves authored motion physics, 3D perspective rail, easing, pointer tracking,
 * wheel scroll, keyboard navigation, and idle harmonic breathing.
 * Customized for GiftVault 'Celebrations Supported Across India' with transparent canvas integration.
 */

(function () {
  'use strict';

  // Global ThreeUI controls object for external control / props
  window.__CHARACTER_CAROUSEL_CONTROLS = {
    speed: 1.0,
    scale: 1.0,
    paused: false
  };

  var CELEBRATION_PROFILES = [
    {
      index: "01",
      name: "Weddings & Receptions",
      role: "Sacred Shagun Registers",
      badge: "WEDDINGS",
      image: "assets/images/concept_12_avant_garde_royal_arch.jpg",
      workspace: "event-wedding"
    },
    {
      index: "02",
      name: "Housewarming",
      role: "Griha Pravesham Blessings",
      badge: "HOUSEWARMING",
      image: "assets/images/concept_5_griha_pravesham_luxury.jpg",
      workspace: "event-housewarming"
    },
    {
      index: "03",
      name: "Silver Jubilee",
      role: "25-Year Milestone Ledger",
      badge: "25-YEAR MILESTONE",
      image: "assets/images/concept_6_silver_jubilee_luxury.jpg",
      workspace: "event-jubilee"
    },
    {
      index: "04",
      name: "Baby Cradle & Naming",
      role: "Traditional Cradle Ceremony",
      badge: "BABY BLESSINGS",
      image: "assets/images/celebration_cradle_clean.jpg",
      workspace: "event-tonsure"
    },
    {
      index: "05",
      name: "Sangeet & Mehendi",
      role: "Musical Gala & Shagun Logs",
      badge: "FESTIVE SANGEET",
      image: "assets/images/concept_4_vibrant_sangeet_gifting.jpg",
      workspace: "event-wedding"
    }
  ];

  // Repeat profiles twice to create a seamless 10-card continuous 3D loop
  var profiles = CELEBRATION_PROFILES.concat(CELEBRATION_PROFILES);

  function initCharacterCarousel() {
    var stage = document.querySelector("#character-filmstrip-stage");
    var deck = document.querySelector("#character-filmstrip-deck");
    if (!stage || !deck) return;

    deck.innerHTML = "";

    var cards = profiles.map(function (profile, index) {
      var card = document.createElement("button");
      card.className = "character-filmstrip-card";
      card.type = "button";
      card.dataset.index = String(index);
      card.dataset.workspace = profile.workspace;
      card.setAttribute("aria-label", "Focus " + profile.name + ", " + profile.role);
      
      card.innerHTML = 
        '<span class="character-card-portrait">' +
          '<img src="' + profile.image + '" alt="' + profile.name + '">' +
          '<span class="character-card-badge">' + profile.badge + '</span>' +
        '</span>' +
        '<span class="character-card-footer">' +
          '<span class="character-card-index">' + profile.index + '</span>' +
          '<span class="character-card-meta">' +
            '<span class="character-card-name">' + profile.name + '</span>' +
            '<span class="character-card-role">Explore Celebration →</span>' +
          '</span>' +
        '</span>';

      deck.appendChild(card);
      return card;
    });

    var count = cards.length;
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    
    var state = {
      phase: 2,
      target: 2,
      base: 2,
      pointerX: 0,
      pointerY: 0,
      active: false,
      lastInput: performance.now()
    };

    function wrappedDelta(index, phase) {
      var delta = index - phase;
      while (delta > count / 2) delta -= count;
      while (delta < -count / 2) delta += count;
      return delta;
    }

    function nearestIndex() {
      return (Math.round(state.phase) % count + count) % count;
    }

    function moveTo(index) {
      var current = nearestIndex();
      var delta = index - current;
      if (delta > count / 2) delta -= count;
      if (delta < -count / 2) delta += count;
      state.base += delta;
      state.target = state.base;
      state.active = false;
      state.lastInput = performance.now();
    }

    cards.forEach(function (card, index) {
      card.addEventListener("click", function () {
        var current = nearestIndex();
        if (current === index) {
          // If already centered, open workspace
          var ws = card.dataset.workspace;
          if (typeof window.openEventWorkspace === "function") {
            window.openEventWorkspace(ws);
          } else if (typeof window.navToView === "function") {
            window.navToView("login");
          }
        } else {
          moveTo(index);
        }
      });
      card.addEventListener("focus", function () {
        moveTo(index);
      });
    });

    // Touch & Pointer Drag mechanics
    var isPointerDown = false;
    var pointerStartX = 0;
    var pointerStartBase = 0;

    stage.addEventListener("pointerdown", function (event) {
      isPointerDown = true;
      pointerStartX = event.clientX;
      pointerStartBase = state.base;
      state.active = true;
      state.lastInput = performance.now();
      try { stage.setPointerCapture(event.pointerId); } catch (e) {}
    });

    stage.addEventListener("pointermove", function (event) {
      if (isPointerDown) {
        var rect = stage.getBoundingClientRect();
        var diff = (event.clientX - pointerStartX) / (rect.width * 0.22);
        state.target = pointerStartBase - diff;
        state.base = state.target;
        state.lastInput = performance.now();
      } else {
        var rect = stage.getBoundingClientRect();
        var nx = Math.max(-1, Math.min(1, ((event.clientX - rect.left) / rect.width - 0.5) * 2));
        var ny = Math.max(-1, Math.min(1, ((event.clientY - rect.top) / rect.height - 0.5) * 2));
        state.pointerX = nx;
        state.pointerY = ny;
        state.active = true;
        state.target = state.base + (window.innerWidth < 650 ? ny * 2.2 : nx * 2.8);
        state.lastInput = performance.now();
      }
    });

    stage.addEventListener("pointerup", function (event) {
      if (isPointerDown) {
        isPointerDown = false;
        state.active = false;
        state.base = Math.round(state.target);
        state.target = state.base;
        try { stage.releasePointerCapture(event.pointerId); } catch (e) {}
      }
    });

    stage.addEventListener("pointercancel", function (event) {
      isPointerDown = false;
      state.active = false;
      state.target = state.base;
    });

    stage.addEventListener("pointerleave", function () {
      if (!isPointerDown) {
        state.active = false;
        state.pointerX = 0;
        state.pointerY = 0;
        state.target = state.base;
      }
    });

    stage.addEventListener("wheel", function (event) {
      var direction = Math.sign(Math.abs(event.deltaY) > Math.abs(event.deltaX) ? event.deltaY : event.deltaX);
      if (!direction) return;
      state.base += direction * 0.8;
      state.target = state.base;
      state.active = false;
      state.lastInput = performance.now();
    }, { passive: true });

    // Keyboard arrow keys
    window.addEventListener("keydown", function (event) {
      var forward = event.key === "ArrowRight" || event.key === "ArrowDown";
      var backward = event.key === "ArrowLeft" || event.key === "ArrowUp";
      if (!forward && !backward) return;
      
      // Only process when #culture is in viewport or active
      var rect = stage.getBoundingClientRect();
      if (rect.top > window.innerHeight || rect.bottom < 0) return;

      state.base += forward ? 1 : -1;
      state.target = state.base;
      state.active = false;
      state.lastInput = performance.now();
    });

    // Prev / Next button listeners
    var btnPrev = document.querySelector("#btn-filmstrip-prev");
    var btnNext = document.querySelector("#btn-filmstrip-next");
    if (btnPrev) {
      btnPrev.addEventListener("click", function () {
        state.base -= 1;
        state.target = state.base;
        state.active = false;
        state.lastInput = performance.now();
      });
    }
    if (btnNext) {
      btnNext.addEventListener("click", function () {
        state.base += 1;
        state.target = state.base;
        state.active = false;
        state.lastInput = performance.now();
      });
    }

    var previousTime = performance.now();

    function render(time) {
      var deltaTime = Math.min(32, time - previousTime);
      previousTime = time;

      var controls = window.__CHARACTER_CAROUSEL_CONTROLS || { speed: 1.0, scale: 1.0, paused: false };
      if (controls.paused) {
        requestAnimationFrame(render);
        return;
      }

      var effectiveDelta = deltaTime * (controls.speed || 1.0);
      var ease = reducedMotion ? 1 : 1 - Math.pow(0.001, effectiveDelta / 1000);

      // Idle harmonic oscillation after 3.6s of inactivity
      if (!state.active && !isPointerDown && time - state.lastInput > 3600) {
        var idle = time - state.lastInput - 3600;
        state.target = state.base + Math.sin(idle * 0.00042) * 2.45;
      }

      state.phase += (state.target - state.phase) * ease;
      var compact = window.innerWidth < 650;
      var activeIndex = nearestIndex();
      var horizontalSpacing = Math.min(195, Math.max(140, window.innerWidth * 0.135));
      var verticalSpacing = Math.min(130, Math.max(90, window.innerHeight * 0.12));

      cards.forEach(function (card, index) {
        var delta = wrappedDelta(index, state.phase);
        var distance = Math.abs(delta);
        var focus = Math.exp(-distance * distance * 1.28);
        var side = Math.max(0, 1 - distance / 5);
        var direction = Math.sign(delta);

        var x = compact
          ? delta * 24 + Math.sin(delta * 0.9) * 25
          : delta * horizontalSpacing;
        var y = compact
          ? delta * verticalSpacing
          : distance * 8 + state.pointerY * focus * 10;
        var z = focus * 155 - distance * 150;
        var scale = (0.56 + side * 0.14 + focus * 0.52) * (controls.scale || 1.0);
        var rotateX = compact ? delta * 2.1 : -state.pointerY * focus * 3.5;
        var rotateY = compact
          ? -delta * 5
          : -direction * (distance > 0.2 ? 14 + Math.min(distance, 3) * 5 : 0) + state.pointerX * focus * 3;
        var rotateZ = compact ? delta * -1.4 : delta * 0.7;

        card.style.setProperty("--focus", focus.toFixed(4));
        card.style.zIndex = String(Math.round(1000 - distance * 100));
        card.style.opacity = String(Math.max(0.18, side * 0.76 + focus * 0.24));
        card.style.filter = "blur(" + (Math.max(0, distance - 1.5) * 0.38) + "px)";
        card.style.transform = [
          "translate(-50%, -50%)",
          "translate3d(" + x.toFixed(2) + "px, " + y.toFixed(2) + "px, " + z.toFixed(2) + "px)",
          "rotateX(" + rotateX.toFixed(2) + "deg)",
          "rotateY(" + rotateY.toFixed(2) + "deg)",
          "rotateZ(" + rotateZ.toFixed(2) + "deg)",
          "scale(" + scale.toFixed(4) + ")"
        ].join(" ");

        card.setAttribute("aria-current", index === activeIndex ? "true" : "false");
      });

      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
  }

  // Auto-init on DOMContentLoaded or immediate if already loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCharacterCarousel);
  } else {
    initCharacterCarousel();
  }

  window.initCharacterCarousel = initCharacterCarousel;
})();
