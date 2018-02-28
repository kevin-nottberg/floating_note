//
//  simple_vector_library.cpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/2/18.
//

#include "simple_vector_library.hpp"
#include <algorithm>
#include <math.h>

//2D Vector
SimpleVector::SimpleVector( float x, float y ) : x_comp(x), y_comp(y), z_comp(0) {};

//3D Vector
SimpleVector::SimpleVector( float x, float y, float z ) : x_comp(x), y_comp(y), z_comp(z) {};

//Addition Methods
void SimpleVector::add( SimpleVector &obj ) {
    this->x_comp += obj.x_comp;
    this->y_comp += obj.y_comp;
    this->z_comp += obj.z_comp;
}

void SimpleVector::add( float x, float y ) {
    this->x_comp += x;
    this->y_comp += y;
}

void SimpleVector::add( float x, float y, float z ) {
    this->x_comp += x;
    this->y_comp += y;
    this->z_comp += z;
}

//Subtraction Methods
void SimpleVector::sub( SimpleVector obj ) {
    this->x_comp -= obj.x_comp;
    this->y_comp -= obj.y_comp;
    this->z_comp -= obj.z_comp;
}

void SimpleVector::sub( float x, float y ) {
    this->x_comp -= x;
    this->y_comp -= y;
}

void SimpleVector::sub( float x, float y, float z ) {
    this->x_comp -= x;
    this->y_comp -= y;
    this->z_comp -= z;
}

//Multipication
void SimpleVector::multi( float scalar ) {
    this->x_comp *= scalar;
    this->y_comp *= scalar;
    this->z_comp *= scalar;
}

//Division
void SimpleVector::div( float scalar ) {
    if(scalar != 0.0) {
        this->x_comp /= scalar;
        this->y_comp /= scalar;
        this->z_comp /= scalar;
    }
}

//Dot-product methods
float SimpleVector::dot( SimpleVector obj ) {
    return (this->x_comp * obj.x_comp + this->y_comp * obj.y_comp, this->z_comp * obj.z_comp);
}

float SimpleVector::dot( float x, float y ) {
    return (this->x_comp * x + this->y_comp * y + this->z_comp * 0);
}

float SimpleVector::dot( float x, float y, float z ) {
    return (this->x_comp * x + this->y_comp * y + this->z_comp * z);
}

SimpleVector SimpleVector::cross( SimpleVector obj ) {
    float cross_x = (this->y_comp * obj.z_comp - this->z_comp * obj.y_comp);
    float cross_y = (this->z_comp * obj.x_comp - this->x_comp * obj.z_comp);
    float cross_z = (this->x_comp * obj.y_comp - this->y_comp * obj.z_comp);
    
    return SimpleVector(cross_x, cross_y, cross_z);
}

SimpleVector SimpleVector::normalize() {
    if(this->mag() == 0.0) {
        return *this;
    } else {
        SimpleVector new_vector = this->copy();
        new_vector.div(new_vector.mag());
        this->x_comp = new_vector.x_comp;
        this->y_comp = new_vector.y_comp;
    }
}

SimpleVector SimpleVector::rotate( float rotation ) {
    float new_heading = this->heading() + rotation;
    float mag = this->mag();
    
    this->x_comp = cos(new_heading) * mag;
    this->y_comp = sin(new_heading) * mag;
    
    return *this;
}

float SimpleVector::dist( SimpleVector obj ) {
    SimpleVector tmp = obj.copy();
    tmp.sub(*this);
    return tmp.mag();
}

void SimpleVector::limit( float lim ) {
    float mSq = (this->x_comp * this->x_comp +
                 this->y_comp * this->y_comp +
                 this->z_comp * this->z_comp);
    if(mSq > lim * lim) {
        this->div(sqrt(mSq));
        this->multi(lim);
    }
    
    return *this;
}

float SimpleVector::mag() {
    return sqrt(this->x_comp * this->x_comp +
                this->y_comp * this->y_comp +
                this->z_comp * this->z_comp);
}

void SimpleVector::setMag( float magn ) {
    this->normalize().multi(magn);
}

float SimpleVector::heading() {
    return atan2(this->y_comp, this->x_comp);
}

float SimpleVector::angleBetween( SimpleVector obj ) {
    float dot_mag_mag = this->dot(obj) / (this->mag() * obj.mag());
    return cos(fmin(1.0, fmax(-1.0, dot_mag_mag)));
}

SimpleVector SimpleVector::copy() {
    return SimpleVector(this->x_comp, this->y_comp, this->z_comp);
}













