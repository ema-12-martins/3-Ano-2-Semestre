#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include <math.h>

float translate=0.0f;
float rotate=0.0f;
float scale=1.0f;



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

void draw_piramid(){
	glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 0.8f, 1.0f);
		glVertex3f(1.0f, 0.0f, 1.0f);
		glVertex3f(0.0f, 2.0f, 0.0f);
		glVertex3f(-1.0f, 0.0f, 1.0f);
	glEnd();

	glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 0.65f, 1.0f);
		glVertex3f(1.0f, 0.0f, -1.0f);
		glVertex3f(0.0f, 2.0f, 0.0f);
		glVertex3f(1.0f, 0.0f, 1.0f);	
	glEnd(); 

	glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 0.5f, 1.0f);
		glVertex3f(-1.0f, 0.0f, -1.0f);
		glVertex3f(0.0f, 2.0f, 0.0f);
		glVertex3f(1.0f, 0.0f, -1.0f);
		
	glEnd(); 

	glBegin(GL_TRIANGLES);
		glColor3f(1.00f, 0.35f, 1.0f);
		glVertex3f(-1.0f, 0.0f, 1.0f);
		glVertex3f(0.0f, 2.0f, 0.0f);
		glVertex3f(-1.0f, 0.0f, -1.0f);
	glEnd();

	//Para desenhar a base
	glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 1.0f, 1.0f);
		glVertex3f(1.0f, 0.0f, 1.0f);
		glVertex3f(1.0f, 0.0f, -1.0f);
		glVertex3f(-1.0f, 0.0f, 1.0f);
	glEnd();

	glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 1.0f, 1.0f);
		glVertex3f(1.0f, 0.0f, -1.0f);
		glVertex3f(-1.0f, 0.0f, -1.0f);
		glVertex3f(-1.0f, 0.0f, 1.0f);
	glEnd();

	


}

void keyboard_inputs(unsigned char key, int x, int y) {
    if(key == 'w') {
        translate += 1;
    } else if (key == 's') {
        translate -= 1;
    } else if (key == 'a') {
        rotate = rotate + 15;
    } else if (key == 'd') {
        rotate = rotate - 15;
    }

	glutPostRedisplay();
}

void keyboard_special_inputs(int key_code, int x, int y){
	switch (key_code){
		case GLUT_KEY_UP:
			if (scale<2){
				scale+=1;
			}
			break;
		case GLUT_KEY_DOWN:
			if (scale>-1){
				scale-=1;
			}
			break;

	}
	glutPostRedisplay();
}

void renderScene(void) {

	// clear buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// set the camera
	glLoadIdentity();
	gluLookAt(5.0,5.0,5.0, 
		      0.0,0.0,0.0,
			  0.0f,1.0f,0.0f);

	// put axis drawing in here
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


	// put the geometric transformations here
	glTranslatef(translate,0.0f,0.0f);
	glRotatef(rotate,0.0f,1.0f,0.0f);
	glScalef(scale,scale,scale);

	// put pyramid drawing instructions here
	draw_piramid();


	// End of frame
	glutSwapBuffers();
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

	
// put here the registration of the keyboard callbacks
glutKeyboardFunc(keyboard_inputs);
glutSpecialFunc(keyboard_special_inputs);


//  OpenGL settings
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_CULL_FACE);
	
// enter GLUT's main cycle
	glutMainLoop();
	
	return 1;
}
