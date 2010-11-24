#ifndef HiggsAnalysis_CombinedLimit_ProfileLikelihood_h
#define HiggsAnalysis_CombinedLimit_ProfileLikelihood_h
/** \class ProfileLikelihood
 *
 * abstract interface for physics objects
 *
 * \author Luca Lista (INFN), from initial implementation by Giovanni Petrucciani (UCSD)
 *
 *
 */
#include "HiggsAnalysis/CombinedLimit/interface/LimitAlgo.h"

class ProfileLikelihood : public LimitAlgo {
public:
  virtual bool run(RooWorkspace *w, RooAbsData &data, double &limit);
  virtual const std::string & name() const {
    static const std::string name("ProfileLikelihood");
    return name;
  }
  virtual boost::program_options::options_description options() {
    boost::program_options::options_description d;
    return d;
  }
private:
};

#endif