from conans import ConanFile, CMake, tools


class ConanlibConan(ConanFile):
    name = "conanlib"
    version = "0.1"
    license = "Apache 2.0"
    author = "Max Neunhoeffer"
    url = "https://arangodb.com"
    description = "just a test"
    topics = ("bla")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    #def source(self):
    #    self.run("git clone https://github.com/neunhoef/conanlib.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [ "conanlib" ]
        self.cpp_info.names["cmake_find_package"] = "conanlib"
        self.cpp_info.names["cmake_find_package_multi"] = "conanlib"
