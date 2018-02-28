//
//  FontManager.cpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/17/18.
//

/*
 Later in development. This class will handle all the font permissions.
 Create instances of all the fonts that are in the fft file in the project
 Then the user can later add fonts to the file and the user will see them
 in the font selector later on
*/
#include "FontManager.hpp"

FontManager::FontManager() {
    //Do fucking nothing
}

void FontManager::setup() {
    this->roboto.load("Roboto/Roboto-Medium.ttf", 14, true, true);
}

void FontManager::drawText(string text, int x, int y) {
    //this->getInstanceOfCurrentFont(this->currentFont).drawString(text, x, y);
    this->roboto.drawString(text, x, y);
}

/*
ofTrueTypeFont::getInstanceOfCurrentFont(string font) {
    return * this->roboto;
}
*/


int FontManager::getWidth(string text) {
    return int(this->roboto.stringWidth(text));
}
