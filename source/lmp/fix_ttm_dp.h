#include "fix_ttm.h"
#include <vector>

namespace LAMMPS_NS {
class FixTTMDP : public FixTTM {
public:
  std::vector<int> get_nodes() const {
    std::vector<int> tmp(3);
    tmp[0] = nxgrid;
    tmp[1] = nygrid;
    tmp[2] = nzgrid;
    return tmp;
  };
  double ***const get_T_electron() const { return T_electron; };
};
} // namespace LAMMPS_NS