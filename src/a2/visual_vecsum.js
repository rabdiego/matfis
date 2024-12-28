/*
RODAR ESTE CÓDIGO NO P5JS
*/ 

/// guardam a posição do mouse no plano cartesiano
var mouseXC, mouseYC = 0

function rand(min, max) {
  // funcao auxiliar para gerar um pixel aleatorio
  return Math.floor(Math.random() * (max - min) + min)
}

function generateVectors(min, max) {
  // função para gerar 3 vetores aleatoriamente
  v1 = [rand(min, max), rand(min, max)]
  v2 = [rand(min, max), rand(min, max)]
  v3 = [rand(min, max), rand(min, max)]
  return [v1, v2, v3]
}

function setup(){
  createCanvas(400,400)  
}

let vecs = generateVectors(-100, 100)

function array_shuffle(array) {
  // função auxiliar para embaralhar um array
  let currentIndex = array.length;

  while (currentIndex != 0) {

    let randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }
}

function mouseClicked() {
  // a ordem dos vetores será embaralhada ao passo que o usuario clica o mouse
  array_shuffle(vecs)
}

function draw(){
  goCartesian()  
  
  colore(64,0,0)
  
  /* variaveis auxiliares para desenhar os vetores a partir
  do ponto final do anterior */
  v1_p_2 = [vecs[0][0] + vecs[1][0], vecs[0][1] + vecs[1][1]]
  v2_p_3 = [v1_p_2[0] + vecs[2][0], v1_p_2[1] + vecs[2][1]]
  
  seta(0, 0, vecs[0][0], vecs[0][1])
  seta(vecs[0][0], vecs[0][1], v1_p_2[0], v1_p_2[1])
  seta(v1_p_2[0], v1_p_2[1], v2_p_3[0], v2_p_3[1])
  
  // a soma final dos vetores, em vermelho forte
  colore(200, 0, 0)
  seta(0, 0, v2_p_3[0], v2_p_3[1])
}

function goCartesian()
{
  background(255)
  
  mouseXC = mouseX - width/2
  mouseYC = height/2 - mouseY
  
  colore(128,0,0)
  seta(0,height/2,width, height/2)
  colore(0,128,0)
  seta(width/2,height,width/2, 0)
  
  translate(width/2,height/2)
  scale(1,-1,1)  
}

/// Atualiza as variáveis globais com as coordenadas do mouse no plano cartesiano
function grabMouse()
{
  mouseXC = mouseX - width/2
  mouseYC = height/2 - mouseY
}

/** Renderiza texto corretamente no plano cartesiano
 *  @param str Texto a ser escrito
 *  @param x Posição horizontal do canto inferior esquerdo texto
 *  @param y Posição vertical do canto inferior esquerdo texto
 */
function texto(str,x,y)
{
  push()
    translate( x, y)
    scale(1,-1)
    translate(-x,-y)
  
    // desenha o texto normalmente
    text(str,x,y)
  pop()
}


/* Define as cores de preenchimento e de contorno com o mesmo valor.
 * Há várias opções de trabalho em RGB nesse caso:
 *  - caso c1,c2,c3 e c4 sejam passados, o efeito padrão é uma cor RGBA
 *  - caso c1,c2 e c3 sejam passados, tem-se uma cor RGB.
 *  - caso c1 e c2 sejam passados, c1 é um tom de cinza e c2 é opacidade.
 *  - caso apenas c1 seja passado, c1 é um tom de cinza.
 */
function colore(c1,c2,c3,c4)
{
  if(c4 != null)
  {
    fill(c1,c2,c3,c4)
    stroke(c1,c2,c3,c4)
    return
  }
  if(c3 != null)
  {
    fill(c1,c2,c3)
    stroke(c1,c2,c3)
    return
  }
  
  if(c2 == null )
  {
    fill(c1)
    stroke(c1)
  }
  else
  {
    fill(c1,c1,c1,c2)
    stroke(c1,c1,c1,c2)
  }    
}

/* Desenha um segmento de reta com seta do ponto (x1,y1) para (x2,y2)
 */
function seta(x1,y1,x2,y2)
{
  // o segmento de reta
  line(x1,y1,x2,y2)
  var dx = x2-x1, dy = y2-y1
  var le = sqrt(dx*dx + dy*dy) // comprimento do vetor
  // o vetor v é unitário paralelo ao segmento, com mesmo sentido
  var vx = dx/le, vy = dy/le
  // o vetor u é unitário e perpendicular ao segmento
  var ux = -vy
  var uy = vx
  // a cabeça triangular
  triangle(x2,y2,
           x2-5*vx+2*ux, y2-5*vy+2*uy,
           x2-5*vx-2*ux, y2-5*vy-2*uy)
}