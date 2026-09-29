#include <iostream>

struct Vector3D  { double x, y, z; };
struct Quaternion { double w, x, y, z; };
struct Screen {};
struct Printer {};
struct ByteStream {};

class Circle
{
public:
    explicit Circle(double rad) : radius{ rad } {}

    double getRadius() const noexcept { return radius; }

    void translate(Vector3D const& v)
    {
        std::cout << "Translate: " << v.x << ", " << v.y << ", " << v.z << "\n";
    }

    void rotate(Quaternion const&)
    {
        std::cout << "Rotate\n";
    }

private:
    double radius;
};

class ScreenDrawer
{
public:
    void draw(Circle const& c, Screen&)
    {
        std::cout << "Drawing circle on screen, radius " << c.getRadius() << "\n";
    }
};

class PrinterDrawer
{
public:
    void draw(Circle const& c, Printer&)
    {
        std::cout << "Printing circle, radius " << c.getRadius() << "\n";
    }
};

class CircleSerializer
{
public:
    void serialize(Circle const& c, ByteStream&)
    {
        std::cout << "Serializing circle, radius " << c.getRadius() << "\n";
    }
};

int main()
{
    Circle circle{ 5.0 };

    circle.translate({ 1, 2, 3 });
    circle.rotate({ 1, 0, 0, 0 });

    Screen screen;
    Printer printer;
    ByteStream stream;

    ScreenDrawer{}.draw(circle, screen);
    PrinterDrawer{}.draw(circle, printer);
    CircleSerializer{}.serialize(circle, stream);
}
