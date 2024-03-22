

#include<stdio.h>
#include<stdlib.h>

#define _USE_MATH_DEFINES
#include <math.h>
#include <vector>

#include <IL/il.h>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glew.h>
#include <GL/glut.h>
#endif

unsigned int t, tw, th;
unsigned char *imageData;

GLuint buffers[100000];

float camX = 00, camY = 30, camZ = 40;
int startX, startY, tracking = 0;

int alpha = 0, beta = 45, r = 50;
float ang_rotate;

void changeSize(int w, int h) {

	// Prevent a divide by zero, when window is too short
	// (you cant make a window with zero width).
	if(h == 0)
		h = 1;

	// compute window's aspect ratio 
	float ratio = w * 1.0 / h;

	// Reset the coordinate system before modifying
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	
	// Set the viewport to be the entire window
    glViewport(0, 0, w, h);

	// Set the correct perspective
	gluPerspective(45,ratio,1,1000);

	// return to the model view matrix mode
	glMatrixMode(GL_MODELVIEW);
} 



void drawTerrain() {
	glEnableClientState(GL_VERTEX_ARRAY);
	
    // colocar aqui o código de desnho do terreno usando VBOs com TRIANGLE_STRIPS
	// Calcula o número total de vértices
    int numVertices = 2*255;

    // Desenha os vértices usando GL_TRIANGLE_STRIP
	for(int i=0;i<numVertices;i++){
		glDrawArrays(GL_TRIANGLE_STRIP, i*numVertices, numVertices);
	}
}

float h(int i, int j){
	return (float)imageData[(i * tw + j)];
}


float altura_final(int px,int pz){
	int x1 = floor(px); 
	int x2 = x1 + 1;
	int z1 = floor(pz); 
	int z2 = z1 + 1;

	float fz = pz - z1;
	float fx = px - x1;

	float h_x1_z = h(x1,z1) * (1-fz) + h(x1,z2) * fz;
	float h_x2_z = h(x2,z1) * (1-fz) + h(x2,z2) * fz;
	float height_xz = h_x1_z * (1 - fx) + h_x2_z * fx;
	return height_xz;

}



void renderScene(void) {

	float pos[4] = {-1.0, 1.0, 1.0, 0.0};

	glClearColor(0.0f,0.0f,0.0f,0.0f);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);

	glLoadIdentity();
	gluLookAt(camX, camY, camZ, 
		      0.0,0.0,0.0,
			  0.0f,1.0f,0.0f);


	// to erase when the terrain is ready
	glPushMatrix();
	glColor3f(0.0f,0.8f,0.0f);
	glTranslatef(-122.5,0,-122.5);
	drawTerrain();
	glPopMatrix();

	//
	//draw donuts
	glColor3f(1.0f, 0.4f, 0.4f);
	glutSolidTorus(1, 2, 8, 16);

	//draw circle
	int ang= 360/8;
	for (int i=0;i<8;i++){
		glPushMatrix();
		glColor3f(0.0f, 0.0f, 0.5f);
		glRotated(ang*i+ang_rotate,0,1,0);
		glTranslatef(10, 2, 0);
		glutSolidTeapot(1.5);
		glPopMatrix();
	}

	//draw other circle
	ang= 360/16;
	for (int i=0;i<16;i++){
		glPushMatrix();
		glColor3f(1.0f, 0.0f, 0.0f);
		glRotated(ang*i-ang_rotate,0,1,0);
		glTranslatef(0, 2, 20);
		glutSolidTeapot(1.5);
		glPopMatrix();
	}
	

	//draw trees
	srand(5);
	int x;
	int z;
	for (int i=0;i<1000;i++){
		x = ((float)rand() / RAND_MAX) * 255;
    	z = ((float)rand() / RAND_MAX) * 255;
		if((x * x) + (z * z) > (25 * 25)){
			glPushMatrix();
			glColor3f(0.6f, 0.3f, 0.0f);
			glTranslatef(-122.5,0,-122.5); //Por causa do terreno estar para o lado
			glTranslatef(x, (int)altura_final(z,x), z);
			glRotatef(-90, 1, 0, 0);
			glutSolidCone(1,6,20,20); //Mudamos y aqui
			glColor3f(0.0f, 0.6f, 0.0f);
			glTranslatef(0, 0, 4);
			glutSolidCone(3,3,20,20); //Mudamos y aqui
			glPopMatrix();
		}
	}


// End of frame
	glutSwapBuffers();
}





void processKeys(unsigned char key, int xx, int yy) {

// put code to process regular keys in here
}



void processMouseButtons(int button, int state, int xx, int yy) {
	
	if (state == GLUT_DOWN)  {
		startX = xx;
		startY = yy;
		if (button == GLUT_LEFT_BUTTON)
			tracking = 1;
		else if (button == GLUT_RIGHT_BUTTON)
			tracking = 2;
		else
			tracking = 0;
	}
	else if (state == GLUT_UP) {
		if (tracking == 1) {
			alpha += (xx - startX);
			beta += (yy - startY);
		}
		else if (tracking == 2) {
			
			r -= yy - startY;
			if (r < 3)
				r = 3.0;
		}
		tracking = 0;
	}
}


void processMouseMotion(int xx, int yy) {

	int deltaX, deltaY;
	int alphaAux, betaAux;
	int rAux;

	if (!tracking)
		return;

	deltaX = xx - startX;
	deltaY = yy - startY;

	if (tracking == 1) {


		alphaAux = alpha + deltaX;
		betaAux = beta + deltaY;

		if (betaAux > 85.0)
			betaAux = 85.0;
		else if (betaAux < -85.0)
			betaAux = -85.0;

		rAux = r;
	}
	else if (tracking == 2) {

		alphaAux = alpha;
		betaAux = beta;
		rAux = r - deltaY;
		if (rAux < 3)
			rAux = 3;
	}
	camX = rAux * sin(alphaAux * 3.14 / 180.0) * cos(betaAux * 3.14 / 180.0);
	camZ = rAux * cos(alphaAux * 3.14 / 180.0) * cos(betaAux * 3.14 / 180.0);
	camY = rAux * 							     sin(betaAux * 3.14 / 180.0);
}


void init() {
    // Load the height map "terreno.jpg"
    ilInit();
    ilGenImages(1, &t);
    ilBindImage(t);
    ilLoadImage((ILstring)"terreno.jpg");
    ilConvertImage(IL_LUMINANCE, IL_UNSIGNED_BYTE);
    tw = ilGetInteger(IL_IMAGE_WIDTH);
    th = ilGetInteger(IL_IMAGE_HEIGHT);
    imageData = ilGetData();
	printf("%d",tw);
	printf("%d",th);
	

    // Build the vertex arrays
    std::vector<float> vertexB;

    // Fill vertexB with data
    for(int i = 0; i < 255; i++) { // Linhas
        for(int j = 0; j < 255; j++) { // Colunas
            vertexB.push_back(j);
            vertexB.push_back(h(i,j));
            vertexB.push_back(i);

            vertexB.push_back(j);
            vertexB.push_back(h(i+1,j));
            vertexB.push_back(i+1);
        }
    }
	int arraySize = sizeof(float) * vertexB.size(); 

	glewInit();
	glEnableClientState(GL_VERTEX_ARRAY);
	glGenBuffers(1, buffers);
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0]);
    glBufferData(GL_ARRAY_BUFFER, arraySize, vertexB.data(), GL_STATIC_DRAW);

    glVertexPointer(3, GL_FLOAT, 0, 0);
    glEnable(GL_DEPTH_TEST);
}



int main(int argc, char **argv) {

// init GLUT and the window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(320,320);
	glutCreateWindow("CG@DI-UM");
		

// Required callback registry 
	glutDisplayFunc(renderScene);
	glutIdleFunc(renderScene);
	glutReshapeFunc(changeSize);

// Callback registration for keyboard processing
	glutKeyboardFunc(processKeys);
	glutMouseFunc(processMouseButtons);
	glutMotionFunc(processMouseMotion);

	init();	

// enter GLUT's main cycle
	glutMainLoop();
	
	return 0;
}

