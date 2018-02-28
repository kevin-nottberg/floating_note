#include "ofApp.h"
#include "bubble.h"

#include "simple_vector_library.hpp"
#include "bubble.h"
#include <iostream>
#include "collision_api.hpp"
#include "expansion_api.hpp"
#include "TextField.hpp"
#include "FontManager.hpp"

using namespace std;

CollisionHandler colHandler;

//Set variables
vector<Bubble> bubbles;
int selectedBubble;
int maxExpansionLength;
int expansionRate;
int numberOfNotes;


RenderState curr_graphics_state;
//--------------------------------------------------------------
void ofApp::setup(){
    
    FontManager testMng = FontManager();
    testMng.setup();
    
    //Initalize the global variables
    roboto.load("Roboto/Roboto-Medium.ttf", 14, true, true);
    lato.load("Lato/Lato-Regular.ttf", 14, true, true);
    montserrat.load("Montserrat/Montserrat-Medium.ttf", 14, true, true);
    open_sans.load("Open_Sans/OpenSans-Regular.ttf", 14, true, true);
    oxygen.load("Oxygen/Oxygen-Regular.ttf", 14, true, true);
    source_sans_pro.load("Source_Sans_Pro/SourceSansPro-Regular.ttf", 14, true, true);
    
    curr_graphics_state = RenderState::floating;
    
    colHandler = CollisionHandler();
        
    expansionRate = 10;
    numberOfNotes = 10;
    
    ofSetFrameRate(60);
    for( int i = 0; i < numberOfNotes; i += 1 ) {
        Bubble bub = Bubble(70, 10, i, 3000);
        bub.setup();
        bubbles.push_back(bub);
    }
}

//--------------------------------------------------------------
void ofApp::update(){
    if(curr_graphics_state == RenderState::floating) {
        for ( int i = 0; i < bubbles.size(); i += 1 ) {
            bubbles[i].update(RenderState::floating);
        }
        
        colHandler.checkForCollisions(bubbles);
    } else if (curr_graphics_state == RenderState::expanding) {
        for ( int i = 0; i < bubbles.size(); i += 1 ) {
            bubbles[i].update(RenderState::expanding);
        }
        
        bubbles[selectedBubble].radius += expansionRate;
        
        if(bubbles[selectedBubble].radius > maxExpansionLength) {
            curr_graphics_state = RenderState::noting;
        }
        
    } else if (curr_graphics_state == RenderState::noting) {

    } else if (curr_graphics_state == RenderState::closing) {
        
    }
}

//--------------------------------------------------------------
void ofApp::draw(){
    ofBackground(5, 127, 232, 150);
    ofSetColor(255);
    ofNoFill();
    if(curr_graphics_state == RenderState::floating) {
        for( int i = 0; i < bubbles.size(); i += 1 ) {
            bubbles[i].draw();
        }
    } else if (curr_graphics_state == RenderState::expanding) {
        for(int i = 0; i < bubbles.size(); i += 1) {
            if(bubbles[i].ID != bubbles[selectedBubble].ID) {
                bubbles[i].draw();
            } else {
                bubbles[selectedBubble].expansiveDraw();
            }
        }
    } else if (curr_graphics_state == RenderState::noting) {
        bubbles[selectedBubble].notingDraw();
    }
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    bubbles[selectedBubble].keyboardInput(key);
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
    if(curr_graphics_state == RenderState::floating) {
        // Check if it the click was inside the bubble
        for( int i = 0; i < bubbles.size(); i += 1 ) {
            if(x <= bubbles[i].position.x_comp + bubbles[i].radius &&
               x >= bubbles[i].position.x_comp - bubbles[i].radius &&
               y <= bubbles[i].position.y_comp + bubbles[i].radius &&
               y >= bubbles[i].position.y_comp - bubbles[i].radius) {
                
                selectedBubble = i;
                calculateSetExpansiveDeltas(bubbles[selectedBubble], bubbles, expansionRate);
                maxExpansionLength = hypoRadiusCorner(bubbles[selectedBubble]);
                
                curr_graphics_state = RenderState::expanding;
                break;
            }
        }
    } else if(curr_graphics_state == RenderState::expanding) {
    }
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){
    
}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
