class Mover {
  constructor() {
    this.position = createVector(random(width), height);
    this.velocity = createVector();
    this.acceleration = createVector();
    this.mass = 10.0;
    this.topspeed = 2;
  }

  update() {
    this.velocity.add(this.acceleration);
    this.velocity.limit(this.topspeed);
    this.position.add(this.velocity);
    this.acceleration.mult(0);
  }

  applyForce(force){
    this.acceleration.add(p5.Vector.div(force, this.mass));
  }

  display() {
    stroke(0);
    strokeWeight(2);
    fill(244);
    ellipse(this.position.x, this.position.y, this.mass + 5, this.mass + 5);
  }
}