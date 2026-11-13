from playwright.sync_api import sync_playwright
import os

test_html = """<!DOCTYPE html>
<html>
<head>
<style>
  body { background: #FAF7F2; padding: 40px; }
  .btn-test {
    position: relative;
    width: 240px;
    height: 52px;
    border-radius: 999px;
    border: none;
    cursor: pointer;
    overflow: hidden;
    background: #8A1526;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .btn-test canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
  .btn-test span {
    position: relative;
    z-index: 2;
    color: #FFFFFF;
    font-family: sans-serif;
    font-weight: 600;
  }
</style>
</head>
<body>
<button class="btn-test" id="btn"><canvas id="gl"></canvas><span>Enter Family Vault</span></button>
<script>
var canvas = document.getElementById('gl');
var gl = canvas.getContext('webgl');
console.log('WebGL supported:', !!gl);
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
  '  vec3 col = mix(vec3(0.48, 0.06, 0.12), vec3(0.38, 0.04, 0.09), uv.y);',
  '  col += vec3(0.15, 0.03, 0.04) * pow(max(0.0, 1.0 - abs(uv.y - 0.88) * 6.0), 2.0);',
  '  float inside = smoothstep(0.0, 0.012, d);',
  '  float depth = clamp(d / max(u_level, 0.001), 0.0, 1.0);',
  '  vec3 liq = mix(vec3(0.68, 0.10, 0.18), vec3(0.40, 0.04, 0.08), depth);',
  '  float caust = fbm(vec2(x * 4.2, (uv.y + t * 0.14) * 4.2));',
  '  liq *= 0.88 + 0.35 * caust;',
  '  liq += vec3(0.35, 0.20, 0.05) * pow(max(0.0, d * 3.0), 1.5) * u_slosh;',
  '  col = mix(col, liq, inside);',
  '  col += vec3(1.0, 0.88, 0.55) * exp(-abs(d) * 85.0) * 0.95;',
  '  col += vec3(1.0, 0.96, 0.80) * exp(-abs(d) * 230.0) * 0.65;',
  '  vec2 e = uv * (1.0 - uv);',
  '  col *= 0.72 + 0.28 * pow(e.x * e.y * 16.0, 0.22);',
  '  gl_FragColor = vec4(col, 1.0);',
  '}'
].join('\\n');

function compile(type, src) {
  var s = gl.createShader(type);
  gl.shaderSource(s, src);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
    console.error('Shader error:', gl.getShaderInfoLog(s));
  }
  return s;
}
var prog = gl.createProgram();
gl.attachShader(prog, compile(gl.VERTEX_SHADER, VS));
gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, FS));
gl.linkProgram(prog);
console.log('Program link status:', gl.getProgramParameter(prog, gl.LINK_STATUS));
</script>
</body>
</html>"""

with open('test_shader.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.on('console', lambda msg: print('Browser console:', msg.text))
    page.goto('file:///' + os.path.abspath('test_shader.html').replace('\\', '/'))
    page.wait_for_timeout(500)
    browser.close()
