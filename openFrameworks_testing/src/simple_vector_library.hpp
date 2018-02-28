//
//  simple_vector_library.hpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/2/18.
//

#ifndef simple_vector_library_hpp
#define simple_vector_library_hpp

#include <stdio.h>

class SimpleVector {
public:
    float x_comp;
    float y_comp;
    float z_comp;
    
    //Two dimensional constructor
    SimpleVector(float x, float y);
    //Three dimensional constructor
    SimpleVector(float x, float y, float z);
    
    SimpleVector copy();
    
    //Operator functions
    void add(SimpleVector &obj);
    void add(float x, float y);
    void add(float x, float y, float z);
    
    void sub(SimpleVector obj);
    void sub(float x, float y);
    void sub(float x, float y, float z);
    
    void multi(float scalar);
    
    void div(float scalar);
    float mag();
    
    float dot(SimpleVector obj);
    float dot(float x, float y);
    float dot(float x, float y, float z);
    
    
    SimpleVector cross(SimpleVector obj);
    SimpleVector normalize();
    SimpleVector rotate(float rot);
    
    float dist(SimpleVector obj);
    
    void limit(float n);
    void setMag(float n);
    float heading();
    float angleBetween(SimpleVector obj);
    
private:
};

#endif /* simple_vector_library_hpp */
