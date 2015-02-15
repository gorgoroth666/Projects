#ifndef COMMON_H
#define COMMON_H


#include <SFML/Graphics.hpp>
#include <sstream>


int clamp (int x, int a, int b)
{
	return std::min(std::max(a,x),b);
}


template <typename T>
std::string toString(const T& value)
{
    std::stringstream stream;
    stream << value;
    return stream.str();
}



bool intersects (const sf::RectangleShape & rect1,const sf::RectangleShape & rect2)
{
    sf::FloatRect r1=rect1.getGlobalBounds();
    sf::FloatRect r2=rect2.getGlobalBounds();
    return r1.intersects (r2);
}


class GameCore
{
public:
    GameCore(int width, int height, const sf::String & name)
    {
        initWindow(width, height, name);
    }

    void initWindow(int width, int height, const sf::String & name)
    {
        sf::VideoMode videoMode(width, height);
        gameWindow.create(videoMode, name);
    }

    void gameEvent()
    {
        sf::Event event;
        while(gameWindow.pollEvent(event))
        {
            if (isQuitRequested(event))
                gameWindow.close();
        }
    }    

    void gameLoop()
    {
        while(gameWindow.isOpen())
        {
            gameWindow.clear(sf::Color(0, 0, 0));
            gameWindow.display();
            gameEvent();            
        }
    }

    static bool isQuitRequested(const sf::Event & e)
    {
        if(e.type == sf::Event::Closed)
            return true;
        if((e.type == sf::Event::KeyPressed) && (e.key.code == sf::Keyboard::Escape))
            return true;
        return false;
    }

protected:
    
    sf::RenderWindow gameWindow;
};




void screenCapture(const sf::RenderWindow & window, const std::string & name)
{
    sf::Image screenshot;
    screenshot = window.capture();
    screenshot.saveToFile(name);
}


#endif