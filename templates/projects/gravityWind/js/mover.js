class Mover {
  constructor(x, y, mass, hasGravity) {
    this.position = createVector(x, y);
    this.velocity = createVector();
    this.acceleration = createVector();
    this.mass = mass;
    this.hasGravity = hasGravity;
    this.gravity = createVector(0, 0);
    if (hasGravity){
      this.gravity = createVector(0, 0.5 * this.mass);
    }
    
    this.topspeed = 2;
  }

  update() {
    this.applyForce(this.gravity);
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