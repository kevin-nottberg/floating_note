//
//  TextField.cpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/9/18.
//

#include "ofApp.h"
#include "TextField.hpp"

TextField::TextField(int x, int y, int width, int height) : position(x, y), dimensions(width, height), cursorPosition(0, 0) {
    this->fntManager = FontManager();
    this->fntManager.setup();
    
    this->completeText = "Hi, this is fucking string init text";
    this->refreshLineArray();
}

void TextField::setPosition(int x, int y) {
    this->position.x_comp = x;
    this->position.y_comp = y;
}

void TextField::setBackgroundColor(int red, int green, int blue, int alpha) {
    this->backgroundColor.push_back(red);
    this->backgroundColor.push_back(green);
    this->backgroundColor.push_back(blue);
    this->backgroundColor.push_back(alpha);
}

void TextField::setFieldPadding(int padding) {
    this->padding = padding;
}

void TextField::draw() {
    //Draw the bounds of the text field
    //Add a shadow
    ofNoFill();
    ofSetLineWidth(3);
    /*
    ofSetColor(this->backgroundColor[0], this->backgroundColor[1],
                        this->backgroundColor[2], this->backgroundColor[3]);
    */
    
    ofDrawRectangle(this->position.x_comp,
                    this->position.y_comp,
                    this->dimensions.x_comp + this->padding,
                    this->dimensions.y_comp + this->padding);
    
    this->fntManager.drawText(this->completeText,
                                this->position.x_comp + this->padding,
                                    this->position.y_comp + this->padding * 2);
}

void TextField::processInput(int key) {
    if(key == OF_KEY_DEL || key == OF_KEY_BACKSPACE) {
        this->completeText = this->completeText.substr(0, this->completeText.length()-1);
    } else if (key == OF_KEY_RETURN) {
        this->completeText += "\n";
    } else if (key == OF_KEY_UP) {
        if(this->cursorPosition.y_comp != 0) {
            this->cursorPosition.y_comp -= 1;
        }
    } else if (key == OF_KEY_DOWN) {
        if(this->cursorPosition.y_comp != lineArray.size()) {
            this->cursorPosition.y_comp += 1;
        }
    } else if (key == OF_KEY_RIGHT) {
        if(this->cursorPosition.x_comp == lineArray[this->cursorPosition.y_comp].length()) {
            this->cursorPosition.x_comp = 0;
            this->cursorPosition.y_comp += 1;
        } else {
            this->cursorPosition.x_comp += 1;
        }
    } else if (key == OF_KEY_LEFT) {
        if(this->cursorPosition.x_comp == 0) {
            this->cursorPosition.x_comp == lineArray[this->cursorPosition.y_comp - 1].length();
            this->cursorPosition.y_comp -= 1;
        } else {
            this->cursorPosition.x_comp -= 1;
        }
    } else {
        if(this->fntManager.getWidth(this->lineArray[this->cursorPosition.y_comp])
           >= this->dimensions.x_comp - this->padding * 2) {
            this->completeText += "\n";
            ofAppendUTF8(this->completeText, key);
            this->cursorPosition.x_comp = 0;
            this->cursorPosition.y_comp += 1;
        } else {
            ofAppendUTF8(this->completeText, key);
            this->cursorPosition.x_comp += 1;
        }
        
        cout << this->lineArray[this->cursorPosition.y_comp] << endl;
        cout << this->fntManager.getWidth(this->lineArray[this->cursorPosition.y_comp]) << endl;
    }
    
    refreshLineArray();
}

void TextField::refreshLineArray() {
    this->lineArray.clear();
    stringstream stream(this->completeText);
    
    while(stream.good()) {
        string newLine;
        getline(stream, newLine, '\n');
        this->lineArray.push_back(newLine);
    }
}


