//
//  expansion_api.cpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/9/18.
//

#include "expansion_api.hpp"

int hypoRadiusCorner(Bubble &selectedBubble) {
    float xLength = 0;
    float yLength = 0;
    
    if(selectedBubble.position.x_comp > (ofGetWindowWidth() / 2)) {
        xLength = selectedBubble.position.x_comp;
    } else {
        xLength = (ofGetWindowWidth() - selectedBubble.position.x_comp);
    }
    
    if(selectedBubble.position.y_comp > (ofGetWindowHeight() / 2)) {
        yLength = selectedBubble.position.y_comp;
    } else {
        yLength = (ofGetWindowHeight() - selectedBubble.position.y_comp);
    }
    
    return int(sqrt((xLength * xLength) + (yLength * yLength)));
}

void calculateSetExpansiveDeltas(Bubble &selectedBubble, vector<Bubble> &bubbles, int expansionRate) {
    selectedBubble.setExpansiveVelocity(0, 0);
    
    for(int i = 0; i < bubbles.size(); i += 1) {
        bubbles[i].preExpansivePos.x_comp = bubbles[i].position.x_comp;
        bubbles[i].preExpansivePos.y_comp = bubbles[i].position.y_comp;
        
        if(bubbles[i].ID != selectedBubble.ID) {
            float deltaX = (selectedBubble.position.x_comp - bubbles[i].position.x_comp) * -1;
            float deltaY = (selectedBubble.position.y_comp - bubbles[i].position.y_comp) * -1;
            
            bubbles[i].setExpansiveVelocity(deltaX, deltaY);
            bubbles[i].expansiveVelocity.normalize();
            bubbles[i].expansiveVelocity.multi(expansionRate);
        }
    }
}

void reverseExpansiveDeltas(vector<Bubble> &bubbles) {
    for(int i = 0; i < bubbles.size(); i += 1) {
        bubbles[i].expansiveVelocity.x_comp *= -1;
        bubbles[i].expansiveVelocity.y_comp *= -1;
    }
}

void expand(Bubble &selectedBubble, int expansionRate) {
    selectedBubble.radius += expansionRate;
    cout<< selectedBubble.radius << endl;
}

void close(Bubble &selectedBubble, int expansionRate) {
    selectedBubble.radius -= expansionRate;
}




