//
//  collision_api.cpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/5/18.
//

#include "collision_api.hpp"
CollisionHandler::CollisionHandler() {};

void CollisionHandler::checkForCollisions(vector<Bubble>& objs) {
    for( int i = 0; i < objs.size(); i += 1 ) {
        for ( int j = i + 1; j < objs.size(); j += 1 ) {
            if(objs[i].ID == objs[j].ID) {
                break;
            } else {
                
                if(this->getDistance(objs[i], objs[j]) <= (objs[i].radius + objs[j].radius + 2)) {
                    
                    float fDistance = getDistance(objs[i], objs[j]);
                    
                    float overlap = 0.6 * (fDistance - objs[i].radius - objs[j].radius);
                    
                    objs[i].position.x_comp -= overlap * (objs[i].position.x_comp - objs[j].position.x_comp) / fDistance;
                    objs[i].position.y_comp -= overlap * (objs[i].position.y_comp - objs[j].position.y_comp) / fDistance;
                    
                    objs[j].position.x_comp += overlap * (objs[i].position.x_comp - objs[j].position.x_comp) / fDistance;
                    objs[j].position.y_comp += overlap * (objs[i].position.y_comp - objs[j].position.y_comp) / fDistance;
                    
                    this->resolveCollisionTwo(objs[i], objs[j]);
                }
            }
        }
    }
}

bool CollisionHandler::isOverlapping(Bubble &one, Bubble &two) {
    float r = one.radius + two.radius;
    r = r * r;
    
    float xDist = two.position.x_comp - one.position.x_comp;
    float yDist = two.position.y_comp - two.position.y_comp;
    
    return (r < xDist * xDist + yDist * yDist);
}

float CollisionHandler::getDistance(Bubble& one, Bubble& two) {
    float xDistance = two.position.x_comp - one.position.x_comp;
    float yDistance = two.position.y_comp - one.position.y_comp;
    
    return sqrt(pow(xDistance, 2) + pow(yDistance, 2));
}

void CollisionHandler::resolveCollision(Bubble& one, Bubble& two) {
    float xDistance = two.position.x_comp - one.position.x_comp;
    float yDistance = two.position.y_comp - one.position.y_comp;
    
    float deltaXVel = two.velocity.x_comp - one.velocity.x_comp;
    float deltaYVel = two.velocity.y_comp - two.velocity.y_comp;
    
    float vx_cm = (one.mass * one.velocity.x_comp + two.mass * two.velocity.x_comp) / (one.mass + two.mass);
    float vy_cm = (one.mass * one.velocity.y_comp + two.mass * two.velocity.y_comp) / (one.mass + two.mass);
    
    if(deltaXVel == 0.0) {
        deltaXVel = 1;
    }
    
    float a = deltaYVel / deltaXVel;
    float dvx2 = -2 * (deltaXVel + a * deltaYVel) / ((1 + a * a) * (1 + (two.mass/one.mass)));
    
    one.velocity.x_comp = one.velocity.x_comp - ((two.mass/one.mass) * dvx2);
    one.velocity.y_comp = one.velocity.y_comp - (a * (two.mass/one.mass) * dvx2);
    
    two.velocity.x_comp = two.velocity.x_comp + dvx2;
    two.velocity.y_comp = two.velocity.y_comp + a * dvx2;
}

void CollisionHandler::resolveCollisionTwo(Bubble &one, Bubble &two) {
    float dist = getDistance(one, two);
    
    float nx = (two.position.x_comp - one.position.x_comp) / dist;
    float ny = (two.position.y_comp - one.position.y_comp) / dist;
    
    float tx = -ny;
    float ty = nx;
    
    float dpTan1 = one.velocity.x_comp * tx + one.velocity.y_comp * ty;
    float dpTan2 = two.velocity.x_comp * tx + two.velocity.y_comp * ty;
    
    float dpNorm1 = one.velocity.x_comp * nx + one.velocity.y_comp * ny;
    float dpNorm2 = two.velocity.x_comp * nx + two.velocity.y_comp * ny;
    
    float m1 = (dpNorm1 * (one.mass - two.mass) + 2.0 * two.mass * dpNorm2) / (one.mass + two.mass);
    float m2 = (dpNorm2 * (two.mass - one.mass) + 2.0 * one.mass * dpNorm1) / (one.mass + two.mass);
    
    one.velocity.x_comp = tx * dpTan1 + nx * m1;
    one.velocity.y_comp = ty * dpTan1 + ny * m1;
    
    two.velocity.x_comp = tx * dpTan2 + nx * m2;
    two.velocity.y_comp = ty * dpTan2 + ny * m2;
}
