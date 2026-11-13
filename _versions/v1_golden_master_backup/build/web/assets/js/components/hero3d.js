/**
 * GiftVault 3D WebGL Hero Coin Scene
 * Powered by Three.js & Studio 3-Point Lighting Formula (Key, Fill, Rim)
 */

window.GVHero3D = {
  init() {
    const container = document.querySelector('.webgl-hero-container');
    const canvas = document.getElementById('three-coin-canvas');
    if (!canvas || !window.THREE || !container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.z = 5.2;

    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // 3-Point Lighting Formula (Studio Grade)
    const keyLight = new THREE.DirectionalLight(0xFFFFFF, 2.2);
    keyLight.position.set(4, 5, 4);
    scene.add(keyLight);

    const fillLight = new THREE.AmbientLight(0xFDE68A, 0.9);
    scene.add(fillLight);

    const rimLight = new THREE.PointLight(0xD4AF37, 3.5, 20);
    rimLight.position.set(-4, -2, -3);
    scene.add(rimLight);

    // Minted Bullion Texture & Luxury Coin Mesh
    const textureLoader = new THREE.TextureLoader();
    const coinTexture = textureLoader.load('assets/images/gv_var_04_minted_bullion_gold_coin_1794318890844.jpg');

    const coinGeo = new THREE.CylinderGeometry(1.65, 1.65, 0.22, 64);
    
    // Multi-material: sides gold, top & bottom minted bullion texture
    const sideMat = new THREE.MeshStandardMaterial({
      color: 0xE5B869,
      metalness: 0.92,
      roughness: 0.18
    });
    const faceMat = new THREE.MeshStandardMaterial({
      map: coinTexture,
      metalness: 0.85,
      roughness: 0.25,
      color: 0xFFF5E0
    });

    const materials = [sideMat, faceMat, faceMat];
    const coin = new THREE.Mesh(coinGeo, materials);
    coin.rotation.x = Math.PI / 2.6;
    scene.add(coin);

    // Ornamental Auric Rim
    const rimGeo = new THREE.TorusGeometry(1.72, 0.05, 16, 64);
    const rimMat = new THREE.MeshStandardMaterial({
      color: 0xFDF0CD,
      metalness: 0.95,
      roughness: 0.12
    });
    const rim = new THREE.Mesh(rimGeo, rimMat);
    coin.add(rim);

    let targetRotY = 0;
    let targetRotX = Math.PI / 2.6;

    window.addEventListener('mousemove', (e) => {
      const mouseX = (e.clientX / window.innerWidth) * 2 - 1;
      const mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
      targetRotY = mouseX * 0.8;
      targetRotX = (Math.PI / 2.6) - (mouseY * 0.4);
    });

    function animate() {
      requestAnimationFrame(animate);
      coin.rotation.z += 0.008; // Continuous auspicious rotation
      coin.rotation.y += (targetRotY - coin.rotation.y) * 0.05;
      coin.rotation.x += (targetRotX - coin.rotation.x) * 0.05;
      renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', () => {
      if (!container.clientWidth || !container.clientHeight) return;
      camera.aspect = container.clientWidth / container.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(container.clientWidth, container.clientHeight);
    });
  }
};
