//
//  bubble.cpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/2/18.
//

#include <stdio.h>
#include <math.h>
#include "bubble.h"


Bubble::Bubble( int radius, int mass, int ID, int resolution )
    :position(0, 0), velocity(0, 0), acceleration(0, 0), preExpansivePos(position.copy()),
        expansiveVelocity(0, 0), textField(100, 100, 800, 800)
{
    this->radius = radius;
    this->mass = mass;
    this->ID = ID;
    this->resolution = resolution;
    
    this->textField = TextField(50, 50, 400, 600);
    this->textField.setFieldPadding(10);
    this->textField.setBackgroundColor(255, 255, 255, 155);
}

void Bubble::setup() {
    
    //Initalize Position and Velocity vector for bubbles
    this->position.x_comp = rand() % (ofGetWindowWidth() - this->radius) + this->radius;
    this->position.y_comp = rand() % (ofGetWindowHeight() - this->radius) + this->radius;
    
    this->velocity.x_comp = rand() % 4;
    this->velocity.y_comp = rand() % 4;
    
    //Generate the current vert list for the bubble resolution
    for( int i = 0; i < this->resolution; i += 1) {
        float theta = (2.0 * 3.145926 * i)/this->resolution;
        float x = this->radius * cos(theta);
        float y = this->radius * sin(theta);
        this->vertList.push_back((x));
        this->vertList.push_back((y));
    }
    
    //Shine Vert list for bubble
    for( int i = 0; i < int( ceil(this->resolution/8) ); ++i ) {
        float theta = 2.0 * 3.145926 * (i/this->resolution);
        
        this->shineVertList.push_back(int( this->radius * cos(theta) ));
        this->shineVertList.push_back(int( this->radius * sin(theta) ));
    }
}

void Bubble::draw() {
    //Draw call here
    ofSetPolyMode(OF_POLY_WINDING_NONZERO);
    ofSetLineWidth(4);
    ofBeginShape();
    for(int i = 0; i < this->vertList.size(); i += 2) {
        ofVertex(this->position.x_comp + this->vertList[i],
                   this->position.y_comp + this->vertList[i + 1]);
        //cout << this->vertList[i] << endl;
    }
    ofEndShape();
    
    ofSetPolyMode(OF_POLY_WINDING_NONZERO);
    ofSetLineWidth(4);
    ofBeginShape();
    for(int i = 0; i < this->shineVertList.size(); i += 2) {
        ofVertex(this->position.x_comp + this->shineVertList[i],
                   this->position.y_comp + this->shineVertList[i + 1]);
    }
    ofEndShape();
}

void Bubble::expansiveDraw() {
    ofSetPolyMode(OF_POLY_WINDING_NONZERO);
    ofSetLineWidth(4);
    ofBeginShape();
    for( int i = 0; i < this->resolution; i += 1 ) {
        float theta = (2.0 * 3.145926 * i)/this->resolution;
        float x = this->radius * cos(theta);
        float y = this->radius * sin(theta);
        ofVertex(this->position.x_comp + x, this->position.y_comp + y);
    }
    ofEndShape();
}

void Bubble::notingDraw() {
    this->textField.draw();
}

void Bubble::update(RenderState state) {
    //Update the vector positioning
    if(state == RenderState::floating) {
        this->position.add(this->velocity);
        if(this->position.x_comp >= ofGetWindowWidth() - this->radius) {
            this->velocity.x_comp *= -1;
            this->position.x_comp = ofGetWindowWidth() - this->radius - 3;
        } else if (this->position.x_comp <= this->radius) {
            this->velocity.x_comp *= -1;
            this->position.x_comp = (this->radius + 3);
        } else if (this->position.y_comp >= ofGetWindowHeight() - this->radius) {
            this->velocity.y_comp *= -1;
            this->position.y_comp = ofGetWindowHeight() - this->radius - 3;
        } else if (this->position.y_comp <= this->radius) {
            this->velocity.y_comp *= -1;
            this->position.y_comp = this->radius + 3;
        }
        
        this->velocity.limit(3);
        this->position.x_comp = (int(this->position.x_comp));
        this->position.y_comp = (int(this->position.y_comp));
    } else if (state == RenderState::expanding) {
        this->position.add(this->expansiveVelocity);
    } else if (state == RenderState::closing) {
        this->position.sub(this->expansiveVelocity);
    }
}

void Bubble::setPosition(int x, int y) {
    this->position.x_comp = x;
    this->position.y_comp = y;
}


void Bubble::keyboardInput(int key) {
    this->textField.processInput(key);
}


void Bubble::setExpansiveVelocity(float x_comp, float y_comp) {
    this->expansiveVelocity.x_comp = x_comp;
    this->expansiveVelocity.y_comp = y_comp;
}
