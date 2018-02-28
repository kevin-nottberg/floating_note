//
//  bubble.h
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/2/18.
//

#ifndef bubble_h
#define bubble_h
#include "simple_vector_library.hpp"
#include "render_states.cpp"
#include "ofApp.h"
#include "TextField.hpp"

class Bubble {
    public:
    
    Bubble(int radius, int mass, int ID, int resolution);
    
    SimpleVector position;
    SimpleVector velocity;
    SimpleVector acceleration;
    
    SimpleVector preExpansivePos;
    SimpleVector expansiveVelocity;
    
    int radius;
    int mass;
    int ID;
    int resolution;
    
    vector<int> vertList;
    vector<int> shineVertList;
    
    void setup();
    void update(RenderState state);
    void draw();
    
    void expansiveDraw();
    
    void notingDraw();
    
    void setPosition(int x, int y);
    void setExpansiveVelocity(float x_comp, float y_comp);
    
    TextField textField;
    
    void keyboardInput(int key);
    
    private:
};
#endif /* bubble_h */
