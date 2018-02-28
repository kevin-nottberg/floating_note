//
//  collision_api.hpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/5/18.
//

#ifndef collision_api_hpp
#define collision_api_hpp

#include <stdio.h>
#include <math.h>
#include "bubble.h"

class CollisionHandler {
public:
    
    void checkForCollisions(vector<Bubble>& objs);
    float getDistance(Bubble& one, Bubble& two);
    void resolveCollision(Bubble& one, Bubble& two);
    
    void resolveCollisionTwo(Bubble &one, Bubble &two);
    
    bool isOverlapping(Bubble &one, Bubble &two);
    
    CollisionHandler();
};

#endif /* collision_api_hpp */
