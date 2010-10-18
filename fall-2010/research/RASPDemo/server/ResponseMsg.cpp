#include "ResponseMsg.h"
#include <boost/algorithm/string.hpp>

using namespace boost;
// Constructor. Zero out the strings.
ResponseMsg::ResponseMsg():Message() {
}

// Constructor to build a request msg from a c raw string. 
ResponseMsg::ResponseMsg(char *s) {
  // parsing the char string into command, param. 
  string str(s);
  int pos; 
  trim(str);
  pos = str.find_first_of(" ");
  // parsing command. 
  if(!pos) cmd_ = str; 		// only command; 
  if(pos > 0) {
    cmd_ = str.substr(0, pos);	// command. 
    cout << "Command is: " << cmd_ << endl;
    str = str.substr(pos+1, str.size() - pos); 
    parseParam(str);
  }
}

// help function for parameter parsing.
// parsing parameters. with the form: 
// [dim d00 d01 d10 d11 ......]
void ResponseMsg::parseParam(string &param) {
  // cout << "Parameters : " << str << endl; 
  char** p;
  double t_dat; 
  int pos;
  pos = param.find_first_of(" ");
  try {
    dim_ = atoi(param.substr(0, pos).c_str());
    cout << "Dimension is: " << dim_ << endl; 
    param = param.substr(pos+1, param.size() - pos);
  } catch(...) {
    cerr << "Error while parsing dimension." << endl;
  }

  // now, data parsing. 
  do {
    pos = param.find_first_of(" ");
    t_dat = strtod(param.substr(0, pos).c_str(), p);
    param = param.substr(pos+1, param.size() - pos).c_str();
    cout << "Data : " << t_dat << endl;
    data_.push_back(t_dat);
  } while(pos > 0);
}

// Return a string representing the command in the message.
string ResponseMsg::getCommand() const {
  return cmd_; 
}

// Return dimension in the cmd msg.
string ResponseMsg::getDimension() const {
}

// get content of data.
string ResponseMsg::getData() const {
   // string temp(parameter2);
   // return temp;
}

// set up command. 
void ResponseMsg::setCommand(string in) {
   // for(int i = 0; i < in.size(); i++)
   // {
   //    command[i] = in[i];
   // }
}
  
// set up dimension info. 
void ResponseMsg::setDimension(string in) {
   // for(int i = 0; i < in.size(); i++)
   // {
   //    parameter1[i] = in[i];
   // }
}
   
// Set up data.
void ResponseMsg::setData(string in) {
}