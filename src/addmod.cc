#include <pybind11/pybind11.h>
#include <add.hpp>

PYBIND11_MODULE(add, m)
{
	m.def("add",&add_int);
}
