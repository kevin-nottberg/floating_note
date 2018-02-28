//
//  FontManager.hpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/17/18.
//

#ifndef FontManager_hpp
#define FontManager_hpp

#include <stdio.h>
#include <string>
#include "ofApp.h"

class FontManager {
    
public:
    
    FontManager();
    
    void setup();
    
    ofTrueTypeFont roboto;
    
    vector<string> getLoadableFonts();
    /*
     Characteristics of the current selected font.
     The manager will load in those fonts dynamically
     as the user changes the current font selection
     and size
    */
    string currentFont;
    string currentFontSize;
    vector<int> color;
    
    void setFont(string font, int size);
    void setCurrFont(string font);
    void setCurrSize(int size);
    
    void setFontColor(int red, int green, int blue);
    
    //Doing fuctions
    void drawText(string text, int x, int y);
    
    int getWidth(string text);
    
private:
    ofTrueTypeFont getInstanceOfCurrentFont(string font);
};

#endif /* FontManager_hpp */
