#include <cmath>
using namespace std;

extern "C"
{
    double WoE(double good, double bad)
    {
        return log(good) / log(bad);
    };
}
