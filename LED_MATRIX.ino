#include <Adafruit_NeoPixel.h>

#define PIN        6
#define NUM_PIXELS 64 // 8x8 matrix
#define MATRIX_WIDTH 8
#define MATRIX_HEIGHT 8

Adafruit_NeoPixel strip(NUM_PIXELS, PIN, NEO_GRB + NEO_KHZ800);

// LMS to RGB conversion matrix
const float LMS_to_RGB[3][3] = {
  {4.4679, -3.5873, 0.1193},
  {-1.2186, 2.3809, -0.1624},
  {0.0497, -0.2439, 1.2045}
};

// LMS Color space matrix
float lmsMatrix[3][3] = {
  {0.5, 0.1, 0.9},
  {0.4, 0.6, 0.4},
  {0.1, 0.5, 0.8}
};


const float CBS_Matrix_Tritanopia[3][3] = {
  {0.9583, 0.0397, 0.002},
  {0.0, 0.9267, 0.0733},
  {0.0, 0.0216, 0.9784}
};

const float CBS_Matrix_Protanopia[3][3] = {
  {0.1708, 0.8282, 0.0},
  {0.0491, 0.9509, 0.0},
  {0.0, 0.0, 1.0}
};

const float CBS_Matrix_Deuteranopia[3][3] = {
  {0.625, 0.375, 0},
  {0.70, 0.30, 0},
  {0, 0.30, 0.70}
};

const float CBS_Matrix_Achromatopsia[3][3] = {
  {0.299, 0.587, 0.114},
  {0.299, 0.587, 0.114},
  {0.299, 0.587, 0.114}
};

const float CBS_Matrix_Normal[3][3] = {
  {1, 0, 0},
  {0, 1, 0},
  {0, 0, 1}
};

void setup() {
  strip.begin();
  strip.show();
  strip.setBrightness(255);
  Serial.begin(9600);
}
// checks for serial connection
void loop() {
  if (Serial.available() > 0) {
  char command = Serial.read();
  if (command == 'P' || command == 'D' || command == 'T') {
    displayGradient(command);
  }
  }
}
// display each color matrix when input from python program is detected
void displayGradient(char command) {
  const float (*CBS_Matrix)[3];
  if (command == 'P') {
    CBS_Matrix = CBS_Matrix_Protanopia;
  } else if (command == 'D') {
    CBS_Matrix = CBS_Matrix_Deuteranopia;
  } else if (command == 'T') {
    CBS_Matrix = CBS_Matrix_Tritanopia;
  } else if (command == 'N') {
    CBS_Matrix = CBS_Matrix_Normal;
  }
    
  float factor;
  uint32_t color;

  for (int y = 0; y < MATRIX_HEIGHT; y++) {
    for (int x = 0; x < MATRIX_WIDTH; x++) {
      factor = float(y * MATRIX_WIDTH + x) / float(NUM_PIXELS - 1);
      color = getGradientColor(lmsMatrix, factor, CBS_Matrix);
      strip.setPixelColor(xyToIndex(x, y), color);
    }
  }
  strip.show();
}
// turn the led matrix into a gradient of the color space
uint32_t getGradientColor(float lmsMatrix[3][3], float factor, const float CBS_Matrix[3][3]) {
  float lms[3];
  float rgb[3];
  float cbs_rgb[3];
  uint8_t r, g, b;

  for (int i = 0; i < 3; i++) {
    lms[i] = lerp(lmsMatrix[0][i], lmsMatrix[2][i], factor);
    rgb[i] = 0;
    for (int j = 0; j < 3; j++) {
      rgb[i] += LMS_to_RGB[i][j] * lms[j];
    }
    rgb[i] = constrain(rgb[i], 0, 1);
  }
  // apply color blindness matrix to rgb 
  for (int i = 0; i < 3; i++) {
    cbs_rgb[i] = 0;
    for (int j = 0; j < 3; j++) {
      cbs_rgb[i] += CBS_Matrix[i][j] * rgb[j];
    }
    cbs_rgb[i] = constrain(cbs_rgb[i], 0, 1);
  }

  r = round(cbs_rgb[0] * 255);
  g = round(cbs_rgb[1] * 255);
  b = round(cbs_rgb[2] * 255);

  return strip.Color(r, g, b);
}

float lerp(float v0, float v1, float t) {
  return v0 + t * (v1 - v0);
}

int xyToIndex(int x, int y) {
  int index;

  if (y % 2 == 0) {
    index = y * MATRIX_WIDTH + x;
  } else {
    index = y * MATRIX_WIDTH + (MATRIX_WIDTH - x - 1);
  }

  return index;
}