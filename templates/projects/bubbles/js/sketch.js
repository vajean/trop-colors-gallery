let movers = [];
let windx = 0.0;
let windy = 0.0;
let densityDeficit;

function setup() {
  createCanvas(640, 360);
  
  for (let i = 0; i < 10; i++) {
    movers[i] = new Mover();
    movers[i].mass = 1+2*i;
  }
  densityDeficit = createVector(0, -0.01);
}

function draw() {

  let wind = createVector(0.0, 0.0);
  wind.add(noise(windx, windy));
  wind.sub(0.5, 0.5);
  wind.div(10);
  background(51);
  for (let i = 0; i < 10; i++){
    movers[i].applyForce(wind);
    movers[i].applyForce(densityDeficit);
    movers[i].update();
    movers[i].display();
  }
  windx += 0.5;
  windy += 0.5;
}