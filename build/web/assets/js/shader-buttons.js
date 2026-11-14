/**
 * ThreeUI <ShaderButtons /> - Tactile Fluidic Button Engine
 * Source revision: SHA-256 6f56c4f91814 (nexus-tactile.html canonical source)
 * Variant: Tactile (tactile-button)
 * Customized with GiftVault Royal Crimson & Sacred Gold fluid physics.
 */

(function () {
  'use strict';

  var VS = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  var FS = [
    'precision highp float;',
    'uniform vec2 u_res;',
    'uniform float u_time;',
    'uniform float u_level;',
    'uniform float u_tilt;',
    'uniform float u_slosh;',
    'float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453123);}',
    'float noise(vec2 p){',
    '  vec2 i=floor(p), f=fract(p);',
    '  vec2 u=f*f*(3.0-2.0*f);',
    '  return mix(mix(hash(i),hash(i+vec2(1.,0.)),u.x),',
    '             mix(hash(i+vec2(0.,1.)),hash(i+vec2(1.,1.)),u.x),u.y);',
    '}',
    'float fbm(vec2 p){',
    '  float v=0.0; float a=0.5;',
    '  for(int i=0;i<4;i++){ v+=a*noise(p); p=p*2.04+vec2(11.3,7.1); a*=0.5; }',
    '  return v;',
    '}',
    'void main(){',
    '  vec2 uv = gl_FragCoord.xy / u_res;',
    '  float ar = u_res.x / u_res.y;',
    '  float x = uv.x * ar;',
    '  float t = u_time;',
    '  float amp = 0.012 + u_slosh * 0.045;',
    '  float surf = u_level',
    '    + u_tilt * (uv.x - 0.5) * 0.34',
    '    + amp * sin(x * 5.1 + t * 4.6)',
    '    + amp * 0.62 * sin(x * 9.7 + t * (-6.8) + 1.7)',
    '    + amp * 0.38 * sin(x * 14.3 + t * 8.9 + 4.2);',
    '  float d = surf - uv.y;',
    '  vec3 col = mix(vec3(0.88, 0.73, 0.35), vec3(0.77, 0.60, 0.22), uv.y);',
    '  col += vec3(0.30, 0.22, 0.05) * pow(max(0.0, 1.0 - abs(uv.y - 0.88) * 6.0), 2.0);',
    '  float inside = smoothstep(0.0, 0.012, d);',
    '  float depth = clamp(d / max(u_level, 0.001), 0.0, 1.0);',
    '  vec3 goldWave = mix(vec3(0.92, 0.78, 0.40), vec3(0.83, 0.68, 0.25), depth);',
    '  vec3 maroonWave = vec3(0.38, 0.05, 0.10);',
    '  vec3 liq = mix(goldWave, maroonWave, clamp(depth * 0.38 + u_slosh * 0.32, 0.0, 0.55));',
    '  float caust = fbm(vec2(x * 4.2, (uv.y + t * 0.14) * 4.2));',
    '  liq *= 0.92 + 0.25 * caust;',
    '  liq += vec3(0.25, 0.20, 0.05) * pow(max(0.0, d * 3.0), 1.5) * u_slosh;',
    '  col = mix(col, liq, inside);',
    '  col += vec3(0.98, 0.92, 0.70) * exp(-abs(d) * 85.0) * 0.95;',
    '  col += vec3(1.0, 0.95, 0.80) * exp(-abs(d) * 230.0) * 0.65;',
    '  vec2 e = uv * (1.0 - uv);',
    '  col *= 0.72 + 0.28 * pow(e.x * e.y * 16.0, 0.22);',
    '  gl_FragColor = vec4(col, 1.0);',
    '}'
  ].join('\n');

  function compileShader(gl, type, src) {
    var s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    return s;
  }

  function initTactileButton(btn) {
    if (!btn) return;
    if (!btn || btn._threeuiMounted) return;
    btn._threeuiMounted = true;

    btn.style.position = 'relative';
    btn.style.overflow = 'hidden';
    btn.style.boxShadow = 'none';

    // Ensure all direct text nodes and child elements have z-index: 10 so they are 100% visible over canvas!
    var childNodes = Array.from(btn.childNodes);
    childNodes.forEach(function (node) {
      if (node.nodeType === 3 && node.textContent.trim().length > 0) {
        // Raw text node: wrap in a styled span
        var span = document.createElement('span');
        span.className = 'btn-tactile-label';
        span.style.position = 'relative';
        span.style.zIndex = '10';
        span.style.color = '#37000A';
        span.style.fontFamily = "'Sen', sans-serif";
        span.style.fontWeight = '800';
        span.style.fontWeight = '700';
        span.style.pointerEvents = 'none';
        span.style.textShadow = 'none';
        span.textContent = node.textContent;
        btn.replaceChild(span, node);
      } else if (node.nodeType === 1 && !node.classList.contains('btn-tactile-gl')) {
        node.style.position = 'relative';
        node.style.zIndex = '10';
        node.style.pointerEvents = 'none';
        if (!node.style.color) {
          node.style.color = '#37000A';
        }
      }
    });

    // Create WebGL canvas
    var canvas = document.createElement('canvas');
    canvas.className = 'btn-tactile-gl';
    canvas.setAttribute('aria-hidden', 'true');
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.borderRadius = 'inherit';
    canvas.style.zIndex = '1';

    btn.insertBefore(canvas, btn.firstChild);

    var gl = canvas.getContext('webgl', { alpha: true, antialias: true, premultipliedAlpha: false });
    if (!gl) {
      btn.style.background = '#8A1526';
      canvas.style.display = 'none';
      return;
    }

    var prog = gl.createProgram();
    gl.attachShader(prog, compileShader(gl, gl.VERTEX_SHADER, VS));
    gl.attachShader(prog, compileShader(gl, gl.FRAGMENT_SHADER, FS));
    gl.linkProgram(prog);
    gl.useProgram(prog);

    var buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);

    var locP = gl.getAttribLocation(prog, 'p');
    gl.enableVertexAttribArray(locP);
    gl.vertexAttribPointer(locP, 2, gl.FLOAT, false, 0, 0);

    var uRes = gl.getUniformLocation(prog, 'u_res');
    var uTime = gl.getUniformLocation(prog, 'u_time');
    var uLevel = gl.getUniformLocation(prog, 'u_level');
    var uTilt = gl.getUniformLocation(prog, 'u_tilt');
    var uSlosh = gl.getUniformLocation(prog, 'u_slosh');

    function resize() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = Math.max(1, Math.round(btn.clientWidth * dpr));
      var h = Math.max(1, Math.round(btn.clientHeight * dpr));
      if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w;
        canvas.height = h;
        gl.viewport(0, 0, w, h);
      }
    }
    resize();
    window.addEventListener('resize', resize);

    var BASE = 0.56;
    var level = BASE;
    var gulp = 0;
    var slosh = 0.35;
    var tilt = 0;
    var tiltTarget = 0;
    var lastX = null;
    var last = performance.now();

    btn.addEventListener('mouseenter', function () {
      slosh = Math.min(1.4, slosh + 0.3);
    });

    btn.addEventListener('mousemove', function (e) {
      var rect = btn.getBoundingClientRect();
      var x = (e.clientX - rect.left) / Math.max(1, rect.width);
      if (lastX !== null) {
        slosh = Math.min(1.4, slosh + Math.abs(x - lastX) * 2.6);
      }
      lastX = x;
      tiltTarget = Math.max(-1, Math.min(1, (x - 0.5) * 2));
    });

    btn.addEventListener('mouseleave', function () {
      lastX = null;
      tiltTarget = 0;
    });

    btn.addEventListener('focus', function () {
      slosh = Math.min(1.4, slosh + 0.4);
    });

    btn.addEventListener('click', function () {
      gulp = 1.0;
      slosh = Math.min(1.4, slosh + 0.7);
    });

    function frame(now) {
      if (!document.body.contains(btn)) {
        return;
      }

      var dt = Math.min(0.05, (now - last) / 1000);
      last = now;

      // Physics damping & spring kinetics
      slosh *= Math.exp(-1.5 * dt);
      gulp *= Math.exp(-1.1 * dt);
      tilt += (tiltTarget - tilt) * Math.min(1, dt * 5.0);
      
      var levelTarget = BASE - 0.34 * gulp;
      level += (levelTarget - level) * Math.min(1, dt * 5.5);

      if (btn.clientWidth > 0 && btn.clientHeight > 0) {
        resize();
        gl.useProgram(prog);
        gl.uniform2f(uRes, canvas.width, canvas.height);
        gl.uniform1f(uTime, now / 1000);
        gl.uniform1f(uLevel, level);
        gl.uniform1f(uTilt, tilt);
        gl.uniform1f(uSlosh, slosh);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      }

      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  function mountAllShaderButtons() {
    var selectors = [
      '.btn-enter-vault',
      '#btn-header-signin',
      '#btn-footer-signin',
      '.btn-tactile-primary',
      '.btn-pricing-activate',
      '.threeui-tactile-btn',
      '.btn-tactile-mount'
    ];

    var buttons = document.querySelectorAll(selectors.join(', '));
    buttons.forEach(function (btn) {
      initTactileButton(btn);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountAllShaderButtons);
  } else {
    mountAllShaderButtons();
  }

  var observer = new MutationObserver(function () {
    mountAllShaderButtons();
  });
  observer.observe(document.body || document.documentElement, { childList: true, subtree: true });

  window.initThreeUIShaderButtons = mountAllShaderButtons;
})();
