#include <bits/stdc++.h>
#include <omp.h>

using namespace std;

#define delT 0.01
#define L 100
#define W 200
#define H 400


int thread_count=1;
int n=1000;
int N=720000;


struct Pos
{
	double x,y,z;
};

struct Vel
{
	double x,y,z;
};

struct Force
{
	double x,y,z;
};


std::vector<Pos> pos(1010);   /// Position vector
std::vector<Vel> vel(1010);	/// Velocity vector
std::vector<Force> force(1010);   ///Force vector


////Function for calculating force at any instance////
void calc_force_n()
{
	//Pos sum;
	double sumx=0;
	double sumy=0;	
	double 	sumz=0;

	#pragma omp parallel for num_threads(thread_count) \
		reduction(+: sumx) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		sumx+=pos[i].x;
	}

	#pragma omp parallel for num_threads(thread_count) \
		reduction(+: sumy) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		sumy+=pos[i].y;
	}

	#pragma omp parallel for num_threads(thread_count) \
		reduction(+: sumz) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		sumz+=pos[i].z;
	}

	#pragma omp parallel for num_threads(thread_count) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{	
		Pos cmass;
		cmass.x=(sumx-pos[i].x)/999;
		cmass.y=(sumy-pos[i].y)/999;
		cmass.z=(sumz-pos[i].z)/999;

		double dx=pos[i].x-cmass.x;
		double dy=pos[i].y-cmass.y;
		double dz=pos[i].z-cmass.z;	

		double d=sqrt(dx*dx + dy*dy + dz*dz);
		double d3=d*d*d;
		
		force[i].x=-(999/d3)*(dx);
		force[i].y=-(999/d3)*(dy);
		force[i].z=-(999/d3)*(dz);	
	}

	return;
}


////Function for calculating half velocity of particle////
void calc_v_half()
{
	#pragma omp parallel for num_threads(thread_count) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		vel[i].x=vel[i].x+(force[i].x/2)*(delT);
		vel[i].y=vel[i].y+(force[i].y/2)*(delT);
		vel[i].z=vel[i].z+(force[i].z/2)*(delT);
	}
	return;
}


////Function for calculating enxt position of the particles////
void calc_next_pos()
{
	#pragma omp parallel for num_threads(thread_count) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		pos[i].x=pos[i].x+(vel[i].x)*delT;
		if(pos[i].x>=L)
		{
			vel[i].x=-vel[i].x;
			pos[i].x=L-0.000001;
		}
		if(pos[i].x<=0)
		{
			vel[i].x=-vel[i].x;
			pos[i].x=0.000001;
		}


		pos[i].y=pos[i].y+(vel[i].y)*delT;
		if(pos[i].y>=W)
		{
			vel[i].y=-vel[i].y;
			pos[i].y=W-0.000001;
		}
		if(pos[i].y<=0)
		{
			vel[i].y=-vel[i].y;
			pos[i].y	=0.000001;		
		}


		pos[i].z=pos[i].z+(vel[i].z)*delT;
		if(pos[i].z>=H)
		{
			vel[i].z=-vel[i].z;
			pos[i].z=H-0.000001;
		}
		if(pos[i].z<=0)
		{
			vel[i].z=-vel[i].z;
			pos[i].z=0.000001;			
		}
	}
	return;
}


////Function for calculating next velocity of particle////
void calc_next_vel()
{
	#pragma omp parallel for num_threads(thread_count) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		vel[i].x=vel[i].x+((force[i].x)/2)*(delT);
		vel[i].y=vel[i].y+((force[i].y)/2)*(delT);
		vel[i].z=vel[i].z+((force[i].z)/2)*(delT);	
	}
	return;
}


int main()
{
	double t1,t2;
	double T1,T2,T3,T4,T5,T6;
	T5=omp_get_wtime();

	cout<<"Please enter the number of threads you want"<<endl;
	cin>>thread_count;
//////////////////////////////FILE READING///////////////////////////////////////////////////////////////////////

	cout<<fixed<<setprecision(6)<<endl; 

	string line;

	int count=0;
	int i=0,j=0;

	ifstream myfile ("file.txt");
	if (myfile.is_open())
	{
              	for (int count = 1; count < 1009; ++count)
              	{
	                    	getline (myfile,line);
	                    	if(count>8)
	                    	{
	                         	istringstream ss(line);   

	                              	string word1,word2,word3; 
	                             	ss>>word1;
		                         ss>>word2;
			            	ss>>word3;
		                              
		                         pos[i].x=stod(word1);
		                         pos[i].y=stod(word2);
		                         pos[i].z=stod(word3);

		                         i++;
	                    	}
               	}
             }
	else 
	{
	           cout<<"Unable to open file";
	}  
	myfile.close();

	///Initializing the velocities of all the 1000 particles/// 
	#pragma omp parallel for num_threads(thread_count) schedule(static ,100)
	for (int i = 0; i < n; ++i)
	{
		vel[i].x=0;
		vel[i].y=0;
		vel[i].z=0;
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	ofstream outfile;
	outfile.open ("trajectory.txt");
	///outfile.open ("trajectory.bin", ios::out | ios::binary); 

//////////////////////////////////LOOP FOR EVERY TIME STAMP/////////////////////////////////////////
	
	////Writing the position at time stamp 0////
	for (int i = 0; i < n; ++i)
	{
		outfile<<pos[i].x<<" "<<pos[i].y<<" "<<pos[i].z<<endl;
	}

	////Calculating F0////
	calc_force_n();

	for (int i = 1; i <= N; ++i)
	{

		t1=omp_get_wtime();		
		calc_v_half();
		t2=omp_get_wtime();
		T1+=(t2-t1);


		t1=omp_get_wtime();		
		calc_next_pos();
		t2=omp_get_wtime();
		T2+=(t2-t1);


		if(i%100==0)
		{
			for (int j = 0; j < n; ++j)
			{
				outfile<<pos[j].x<<" "<<pos[j].y<<" "<<pos[j].z<<endl;
			}
		}


		t1=omp_get_wtime();
		calc_force_n();
		t2=omp_get_wtime();
		T3+=(t2-t1);


		t1=omp_get_wtime();		
		calc_next_vel();
		t2=omp_get_wtime();
		T4+=(t2-t1);
	}

	T6=omp_get_wtime();
	cout<<"Thread(s) used= "<<thread_count<<endl;
	cout<<"Total time for calculating half velocity = "<<T1<<endl;
	cout<<"Total time for calculating next position = "<<T2<<endl;
	cout<<"Total time for calculating force = "<<T3<<endl;
	cout<<"Total time for calculating next velocity = "<<T4<<endl;
	cout<<"Total time for doing all the calculations = "<<T1+T2+T3+T4<<endl;
	cout<<"Total time for executing the program including reading and writing to the file as well  = "<<T6-T5<<endl;

	
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

 	outfile.close();

	return 0;
}


