Name:           ros-indigo-task-compiler
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS task_compiler package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/task_compiler
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-pddl-planner
Requires:       ros-indigo-roseus-smach
BuildRequires:  ros-indigo-catkin

%description
task_compiler Compiler that translate task description in PDDL (Planning Domain
Description Language) to SMACH (state machine based execution and coordination
system) description.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 31 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.3-0
- Autogenerated by Bloom

