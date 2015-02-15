#ifdef _MSC_VER  
	#ifdef _WIN32
		#ifndef _DEBUG
			#pragma comment( lib, "sfml-system.lib" )		
			#pragma comment( lib, "sfml-graphics.lib" )			
			#pragma comment( lib, "sfml-window.lib" )	
		#else
			#pragma comment( lib, "sfml-system-d.lib" )		
			#pragma comment( lib, "sfml-graphics-d.lib" )			
			#pragma comment( lib, "sfml-window-d.lib" )	
		#endif
	#endif
#endif

#include <SFML\Graphics.hpp>
#include "../common/common.h"



class Grid: public sf::FloatRect
{
public:
	unsigned int rows;
	unsigned int columns;

	Grid()
	{
		rows=1;
		columns=1;
	}

    Grid(const int & r,  const int & c)
	{
		rows = r;
		columns = c;
	}

	sf::Vector2f cellSize()
	{
		return sf::Vector2f(width/columns,height/rows);
	}

	void display (sf::RenderWindow & window)
	{
		for (unsigned int i=0;i<rows;i++)
			for (unsigned int j=0;j<columns;j++)
			{
				sf::RectangleShape r(cellSize());
				r.setFillColor(sf::Color::Blue);
				r.setOutlineColor(sf::Color::Black);
				r.setOutlineThickness(3);
				r.setPosition(left+j*cellSize().x, top+i*cellSize().y);
				window.draw(r);
			}
	}

};


int main()
{

    const int windowWidth = 800;
    const int windowHeight = 600;

	sf::VideoMode videoMode(windowWidth, windowHeight, 32);
	sf::RenderWindow renderWindow(videoMode,"Snake Image");
    renderWindow.setFramerateLimit(60);

    const int spriteWidth = 72;
    const int spriteHeight = 72;

    sf::Texture textureTail;
    sf::Texture textureBody;
    sf::Texture textureHead;

    if (!textureTail.loadFromFile("../resource/snake.png", sf::IntRect(0, 0, spriteWidth, spriteHeight)))
	{	
		return EXIT_FAILURE;
	}
    if (!textureBody.loadFromFile("../resource/snake.png", sf::IntRect(spriteWidth, 0, spriteWidth, spriteHeight)))
	{	
		return EXIT_FAILURE;
	}
    if (!textureHead.loadFromFile("../resource/snake.png", sf::IntRect(spriteWidth*2, 0, spriteWidth, spriteHeight)))
	{	
		return EXIT_FAILURE;
	}

	sf::Sprite sprite;
	sprite.setTexture(textureTail);	
    sprite.setPosition(spriteWidth/2,spriteHeight);
    sprite.setScale (0.5f,0.5f);
    
    
    sf::Sprite sprite2;
	sprite2.setTexture(textureBody);	
    sprite2.setPosition(2*spriteWidth/2, spriteHeight);
    sprite2.setScale (0.5f,0.5f);
    

    sf::Sprite sprite3;
	sprite3.setTexture(textureHead);	
    sprite3.setPosition(3*spriteWidth/2, spriteHeight);
    sprite3.setScale (0.5f,0.5f);


    Grid grid(16, 16);
    grid.top = 0;
    grid.left = 0;
    grid.width = spriteWidth/2 * grid.rows;
    grid.height = spriteHeight/2 * grid.columns;


	while (renderWindow.isOpen())
    {

        renderWindow.clear(sf::Color(0, 0, 255));
        grid.display(renderWindow);
		renderWindow.draw(sprite);
        renderWindow.draw(sprite2);
        renderWindow.draw(sprite3);
        renderWindow.display();		        

        sf::Event wEvent;
		while (renderWindow.pollEvent(wEvent))
        {
            if (GameCore::isQuitRequested(wEvent))
			{
                screenCapture(renderWindow, "screenshot.png");
                renderWindow.close();
			}
        }

    }
	
    return EXIT_SUCCESS;
}

