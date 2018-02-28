//
//  expansion_api.hpp
//  openFrameworks_testing
//
//  Created by Kevin Nottberg on 2/9/18.
//

#ifndef expansion_api_hpp
#define expansion_api_hpp

#include <stdio.h>
#include <math.h>
#include "simple_vector_library.hpp"
#include "bubble.h"

int hypoRadiusCorner(Bubble &selectedBubble);

void calculateSetExpansiveDeltas(Bubble &selectedBubble, vector<Bubble> &bubbles, int expansionRate);

void reverseExpansiveDeltas(vector<Bubble> &bubbles);

void expand(Bubble &selectedBubble, int expansionRate);
void close(Bubble &selectedBubble, int expansionRate);


#endif /* expansion_api_hpp */
