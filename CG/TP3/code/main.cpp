#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#define _USE_MATH_DEFINES
#include <math.h>

float alpha=0.0f;
float beta=0.0f;
float rad=5.0f;

void changeSize(int w, int h) {

	// Prevent a divide by zero, when window is too short
	// (you cant make a window with zero width).
	if(h == 0)
		h = 1;

	// compute window's aspect ratio 
	float ratio = w * 1.0 / h;

	// Set the projection matrix as current
	glMatrixMode(GL_PROJECTION);
	// Load Identity Matrix
	glLoadIdentity();
	
	// Set the viewport to be the entire window
    glViewport(0, 0, w, h);

	// Set perspective
	gluPerspective(45.0f ,ratio, 1.0f ,1000.0f);

	// return to the model view matrix mode
	glMatrixMode(GL_MODELVIEW);
}


void drawCylinder(float radius, float height, int slices) {
	// Para desenhar os eixos
	glBegin(GL_LINES);
		// X axis in red
		glColor3f(1.0f, 0.0f, 0.0f);
		glVertex3f(-100.0f, 0.0f, 0.0f);
		glVertex3f( 100.0f, 0.0f, 0.0f);
		// Y Axis in Green
		glColor3f(0.0f, 1.0f, 0.0f);
		glVertex3f(0.0f, -100.0f, 0.0f);
		glVertex3f(0.0f, 100.0f, 0.0f);
		// Z Axis in Blue
		glColor3f(0.0f, 0.0f, 1.0f);
		glVertex3f(0.0f, 0.0f, -100.0f);
		glVertex3f(0.0f, 0.0f, 100.0f);
	glEnd();

	// Para desenhar o cilindro
	float alpha=2*M_PI/slices;
	for(int i = 1; i < slices+1; i++){

		//Bases
		glBegin(GL_TRIANGLES);
			glColor3f(1.0f, 0.8f, 1.0f);
			glVertex3f(cos((i-1)*alpha)*radius,height/2, sin((i-1)*alpha)*radius);
			glVertex3f(0.0f, height/2, 0.0f);
			glVertex3f(cos(i*alpha)*radius,height/2, sin(i*alpha)*radius);
		glEnd();

		glBegin(GL_TRIANGLES);
			glColor3f(1.0f, 0.8f, 1.0f);
			glVertex3f(cos(i*alpha)*radius,-height/2, sin(i*alpha)*radius);
			glVertex3f(0.0f, -height/2, 0.0f);
			glVertex3f(cos((i-1)*alpha)*radius,-height/2, sin((i-1)*alpha)*radius);
		glEnd();

		//Laterais
		glBegin(GL_TRIANGLES);
			glColor3f(1.0f, 0.8f, 1.0f);
			glVertex3f(cos(i*alpha)*radius,-height/2, sin(i*alpha)*radius);
			glVertex3f(cos((i-1)*alpha)*radius, -height/2, sin((i-1)*alpha)*radius);
			glVertex3f(cos((i-1)*alpha)*radius,height/2, sin((i-1)*alpha)*radius);
		glEnd();

		glBegin(GL_TRIANGLES);
			glColor3f(1.0f, 0.8f, 1.0f);
			glVertex3f(cos(i*alpha)*radius,height/2, sin(i*alpha)*radius);
			glVertex3f(cos(i*alpha)*radius,-height/2, sin(i*alpha)*radius);
			glVertex3f(cos((i-1)*alpha)*radius, height/2, sin((i-1)*alpha)*radius);
		glEnd();
		
	}
}


void renderScene(void) {

	// clear buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// set the camera


	glLoadIdentity();
	float pz=cos(alpha)*rad*cos(beta);
	float px=sin(alpha)*rad*cos(beta);
	float py=sin(beta)*rad;

	gluLookAt(px,py,pz, //Posicao da camara
		      0.0f,0.0f,0.0f, //Para onde esta a olhar
			  0.0f,1.0f,0.0f); //Inclinacao da camara

	drawCylinder(1,2,10);

	// End of frame
	glutSwapBuffers();
}


void processKeys(unsigned char c, int xx, int yy) {
	if(c== '-') {
        rad += 1;
    } else if (c == '+') {
		rad -= 1;
	}
	glutPostRedisplay(); 
}


void processSpecialKeys(int key, int xx, int yy) {
	switch (key){
		case GLUT_KEY_UP:
			beta+=0.2;
			break;
		case GLUT_KEY_DOWN:
			beta-=0.2;
			break;
		case GLUT_KEY_RIGHT:
			alpha-=0.2;
			break;
		case GLUT_KEY_LEFT:
			alpha+=0.2;
			break;
	}
	glutPostRedisplay();
}


int main(int argc, char **argv) {

// init GLUT and the window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(800,800);
	glutCreateWindow("CG@DI-UM");
		
// Required callback registry 
	glutDisplayFunc(renderScene);
	glutReshapeFunc(changeSize);
	
// Callback registration for keyboard processing
	glutKeyboardFunc(processKeys);
	glutSpecialFunc(processSpecialKeys);

//  OpenGL settings
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_CULL_FACE);
	glPolygonMode(GL_FRONT_AND_BACK,GL_LINE);
	
// enter GLUT's main cycle
	glutMainLoop();
	
	return 1;
}
