Name:           ros-indigo-pddl-planner
Version:        0.1.4
Release:        1%{?dist}
Summary:        ROS pddl_planner package

Group:          Development/Libraries
License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-downward
Requires:       ros-indigo-ff
Requires:       ros-indigo-ffha
Requires:       ros-indigo-pddl-msgs
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-downward
BuildRequires:  ros-indigo-ff
BuildRequires:  ros-indigo-ffha
BuildRequires:  ros-indigo-pddl-msgs
BuildRequires:  ros-indigo-rospy

%description
pddl planner wrappers

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
* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.4-1
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.4-0
- Autogenerated by Bloom

* Sat Jan 31 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.3-0
- Autogenerated by Bloom

