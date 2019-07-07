let movers = [];
let windx = 0.0;
let windy = 0.0;
let gravity;

function setup() {
  createCanvas(640, 360);
  
  for (let i = 0; i < 10; i++) {
    movers[i] = new Mover(random(width), 0, random(3,10), true);
  }
}

function draw() {

  let wind = createVector(0.0, 0.0);
  wind.add(noise(windx, windy));
  wind.sub(0.5, 0.5);
  wind.div(0.5);
  background(51);
  for (let i = 0; i < 10; i++){
    movers[i].applyForce(wind);
    movers[i].update();
    movers[i].display();
  }
  windx += 0.5;
  windy += 0.5;
}