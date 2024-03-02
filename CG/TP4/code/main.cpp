#include <stdio.h>
#include <stdlib.h>
#include <GL/glew.h>
#include <GL/glut.h>
#include <math.h>

#define _USE_MATH_DEFINES

int timebase;
float frame;
float time;
float fps;
char formattedString[64];
GLuint buffers[1];
int sides = 16; // Número de lados do cilindro
int height = 20; // Altura do cilindro
int vertices;

float alfa = 0.0f, beta = 1.0f, radius = 1.0f; // Definindo beta para M_PI_2 para olhar de cima
float camX = 60.0f, camY = 0.0f, camZ = 0.0f; // Movendo a câmera para cima e para fora do cilindro


void spherical2Cartesian() {
    camX = radius * cos(beta) * sin(alfa);
    camY = radius * sin(beta);
    camZ = radius * cos(beta) * cos(alfa);
}

void changeSize(int w, int h) {
    if (h == 0)
        h = 1;

    float ratio = (float)w / (float)h;

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, ratio, 1.0f, 100.0f); // Reduzido o valor do far plane para evitar corte

    glViewport(0, 0, w, h);

    glMatrixMode(GL_MODELVIEW);
}

void renderScene(void) {
    frame++;
    time = glutGet(GLUT_ELAPSED_TIME);
    if (time - timebase > 1000) {
        fps = frame * 1000.0 / (time - timebase);
        timebase = time;
        frame = 0;
    }
    sprintf(formattedString, "Frames: %f FPS: %f", frame, fps);
    glutSetWindowTitle(formattedString);

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(camX, camY, camZ,
              0.0, 0.0, 0.0,
              0.0f, 1.0f, 0.0f);

    glBindBuffer(GL_ARRAY_BUFFER, buffers[0]);
    glVertexPointer(3, GL_FLOAT, 0, 0);
    glDrawArrays(GL_TRIANGLES, 0, vertices);

    glutSwapBuffers();
}

void processSpecialKeys(int key, int xx, int yy) {
    switch (key) {
    case GLUT_KEY_RIGHT:
        alfa -= 0.1;
        break;
    case GLUT_KEY_LEFT:
        alfa += 0.1;
        break;
    case GLUT_KEY_UP:
        beta += 0.1f;
        if (beta > 1.5f)
            beta = 1.5f;
        break;
    case GLUT_KEY_DOWN:
        beta -= 0.1f;
        if (beta < -1.5f)
            beta = -1.5f;
        break;
    case GLUT_KEY_PAGE_DOWN:
        radius -= 0.1f;
        if (radius < 0.1f)
            radius = 0.1f;
        break;
    case GLUT_KEY_PAGE_UP:
        radius += 0.1f;
        break;
    }
    spherical2Cartesian();
    glutPostRedisplay();
}

void printInfo() {
    printf("Vendor: %s\n", glGetString(GL_VENDOR));
    printf("Renderer: %s\n", glGetString(GL_RENDERER));
    printf("Version: %s\n", glGetString(GL_VERSION));

    printf("\nUse Arrows to move the camera up/down and left/right\n");
    printf("Page Up and Page Down control the distance from the camera to the origin");
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(800, 800);
    glutCreateWindow("CG@DI-UM");

    timebase = glutGet(GLUT_ELAPSED_TIME);

    glutDisplayFunc(renderScene);
    glutReshapeFunc(changeSize);
    glutIdleFunc(renderScene);
    glutSpecialFunc(processSpecialKeys);

    glewInit();

    glEnableClientState(GL_VERTEX_ARRAY);

    vertices = sides * 3 + sides * 6 + sides * 3;
    float *vertexB = (float*)malloc(sizeof(float) * vertices * 3);
    if (vertexB == NULL) {
        printf("Erro ao alocar memória.\n");
        return -1;
    }

    float step = 360.0 / sides;
    int contador = 0;
    for (int i = 0; i < sides; i++) {
        // Topo do cilindro
        vertexB[contador++] = 0;
        vertexB[contador++] = height * 0.5;
        vertexB[contador++] = 0;

        vertexB[contador++] = cos(i * step * M_PI / 180.0) * radius;
        vertexB[contador++] = height * 0.5;
        vertexB[contador++] = -sin(i * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos((i + 1) * step * M_PI / 180.0) * radius;
        vertexB[contador++] = height * 0.5;
        vertexB[contador++] = -sin((i + 1) * step * M_PI / 180.0) * radius;

        // Base do cilindro
        vertexB[contador++] = 0;
        vertexB[contador++] = -height * 0.5;
        vertexB[contador++] = 0;

        vertexB[contador++] = cos((i + 1) * step * M_PI / 180.0) * radius;
        vertexB[contador++] = -height * 0.5;
        vertexB[contador++] = -sin((i + 1) * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos(i * step * M_PI / 180.0) * radius;
        vertexB[contador++] = -height * 0.5;
        vertexB[contador++] = -sin(i * step * M_PI / 180.0) * radius;

        // Lateral do cilindro
        vertexB[contador++] = cos(i * step * M_PI / 180.0) * radius;
        vertexB[contador++] = height * 0.5;
        vertexB[contador++] = -sin(i * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos((i + 1) * step * M_PI / 180.0) * radius;
        vertexB[contador++] = height * 0.5;
        vertexB[contador++] = -sin((i + 1) * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos((i + 1) * step * M_PI / 180.0) * radius;
        vertexB[contador++] = -height * 0.5;
        vertexB[contador++] = -sin((i + 1) * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos(i * step * M_PI / 180.0) * radius;
        vertexB[contador++] = height * 0.5;
        vertexB[contador++] = -sin(i * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos((i + 1) * step * M_PI / 180.0) * radius;
        vertexB[contador++] = -height * 0.5;
        vertexB[contador++] = -sin((i + 1) * step * M_PI / 180.0) * radius;

        vertexB[contador++] = cos(i * step * M_PI / 180.0) * radius;
        vertexB[contador++] = -height * 0.5;
        vertexB[contador++] = -sin(i * step * M_PI / 180.0) * radius;
    }

    glGenBuffers(1, &buffers[0]);
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0]);
    glBufferData(GL_ARRAY_BUFFER, sizeof(float) * 3 * vertices, vertexB, GL_STATIC_DRAW);

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_CULL_FACE);
    glPolygonMode(GL_FRONT, GL_LINE);

    spherical2Cartesian();

    printInfo();

    free(vertexB);

    glutMainLoop();

    return 1;
}
