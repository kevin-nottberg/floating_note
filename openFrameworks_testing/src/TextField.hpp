//
//  TextField.hpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/9/18.
//

#ifndef TextField_hpp
#define TextField_hpp

#include <stdio.h>
#include "ofApp.h"
#include <string>
#include "simple_vector_library.hpp"
#include "FontManager.hpp"

using namespace std;

class TextField {
public:
    //Multi-line
    TextField(int x, int y, int width, int height);
    
    FontManager fntManager;
    
    //Text Field settings
    void setPosition(int x, int y);
    void setBackgroundColor(int red, int green, int blue, int alpha);
    void setFieldPadding(int padding);
    
    vector<int> backgroundColor;
    SimpleVector position;
    SimpleVector dimensions;
    
    int padding;
    
    string completeText;
    vector<string> lineArray;
    
    void draw();
    
    bool isSelected = false;
    
    //Cursor Position is going to be a vector
    //Positiong that will store the character number
    //in the x_comp and lineNumber in the y_comp
    SimpleVector cursorPosition;
    
    void processInput(int key);
    
private:
    
    void refreshLineArray();

};
#endif /* TextField_hpp */
