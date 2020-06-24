/*#include <iostream>
#include <sensor_msgs/PointCloud2.h>
#include <geometry_msgs/PoseStamped.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/registration/ndt.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/voxel_grid.h>
*/
/* #include <pcl/filters/approximate_voxel_grid.h> */
//#include <pcl/visualization/cloud_viewer.h>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;
#include <list>
#include <math.h>

class pcl{
  public:
    //pcl();
    void process();
    // 色々変数
    int pub = 10;
    int get_pri_value();
    int pub2 = 100;


  private:
    // callback
    int pri = 30;
    // method
    int get_pub_value2();

    // parameter
    int call_pub2();
    // member メッセージ的な


};

int pcl::get_pri_value(){
  return pri;
}

int pcl::get_pub_value2(){
  return pub2;
}

int pcl::call_pub2(){
  std::cout << get_pub_value2() << std::endl;

}

void pcl::process(){
  printf("aaaaaa\n");
  call_pub2();
}

int main(){
  int a[5] = {1,2,3,4,5};
  std::cout << sizeof(a) / sizeof(a[0]) << std::endl;// 5
  pcl st;
  std::cout << st.pub << std::endl; // 10
  //std::cout << st.pri << std::endl; <- エラーが出る private内はクラスの中から操作しなければならない
  std::cout << st.get_pri_value() << std::endl; // 30
  //st.call_pub2();
  pcl ss;
  ss.process();
  return 0;
}
