#include<iomanip>
#include<algorithm>
#include<iostream>
#include<fstream>
#include<cstring>
#include<cctype>
#include<string>
#include<vector>
#include <sstream>
using namespace std;

string remove_punct(const string& str){
  string temp = "";
  for(int i = 0; i < str.size(); i++)
    {
      if (!(str[i] == ',') and !(str[i] == '\t')){
	temp += str[i];
      }
    }
  return temp;
}

vector<string> split(const string &str)
{
    vector<string> subs ;
    
    istringstream i(str);

    string sub;
    while ( i >> sub )
        subs.push_back(sub);

    return subs;
}
  
bool is_number(const string& s)
 {
  for(int i = 0; i < s.size(); i++)
    {
      if (!isdigit(s[i]))
	return false;
    }
  return true;
 }

bool has_gene (const string& c)
{
  if(c.find("gene") < 9999999999999)
    return true;
}

//Very simple and hacky hopefully the tbl format from mfannot doesn't change
//Can be improved by adding more information to the gff
int main(int argc,  char **argv)
{
  string file=argv[1];
  string in,  in1,  in2,  in3,  in4;
  fstream fout;
  vector<string> input,  line,  line1,  line2,  line3,  line4;

  fout.open(file);
  while(getline(fout,in)){
    input.push_back(in);
  }

  cout << "##gff-version 3" << endl;

  int id  = 0;
  for(int i = 1; i < input.size()-5;i+=4){
    line = split(input[i]);
    line1 = split(input[i+1]);
    line2 = split(input[i+2]);
    line3 = split(input[i+3]);
    line4 = split(input[i+4]);
    //begin if statement madness seems messy but works for this file format.
    if (has_gene (input[i])){
      bool hasnum = false;
      for(int i = 0; i < line.size();i++){
	if(is_number(line[i]))
	  hasnum = true;
      }
      if(hasnum){
	id++;
	cout << "Balb1" << " . " << " gene " << line[0] << " " << line[1]
	     << " . " << " + " << " . " << "ID=gene" << id <<";Name=" << line1[1] << endl;
      }
	  
	
    }
    if (has_gene (input[i+1])){
      bool hasnum = false;
      for(int i = 0; i < line1.size();i++){
	if(is_number(line1[i]))
	  hasnum = true;
      }
      if(hasnum){
	id++;
	cout << "Balb1" << " . " << " gene " << line1[0] << " "<<  line1[1]
	     << " . " << " + " << " . " << "ID=gene" << id << ";Name=" << line2[1] << endl;
      }

    }
    if (has_gene (input[i+2])){
      
      bool hasnum = false;
      for(int i = 0; i < line2.size();i++){
	if(is_number(line2[i]))
	  hasnum = true;
      }
      if(hasnum){
	id++;
	cout << "Balb1" << " . " << " gene " << line2[0] << " "<<line2[1]
	     << " . " << " + " << " . " << "ID=gene" << id<< ";Name=" << line3[1] << endl;
      }

      
    }
    if (has_gene (input[i+3])){
      bool hasnum = false;
      for(int i = 0; i < line3.size();i++){
	if(is_number(line3[i]))
	  hasnum = true;
      }
      if(hasnum){
	id++;
	cout << "Balb1" << " . " << " gene " << line3[0] << " " <<line3[1]
	     << " . " << " + " << " . " << "ID=gene" << id << ";Name=" << line4[1] << endl;
      }


    }
    
    
  }
}
