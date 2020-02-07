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

    def source(self):
        self.run("git clone https://github.com/neunhoef/conanlib.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="conanlib")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src=".")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["conanlib.a"]

