#include <ilcplex/ilocplex.h>

ILOSTLBEGIN

IloInt nbtw,nbth,nbf, H, L, a, b;
IloNum theta1, theta2;

void define_data(IloEnv env) {
        nbtw = 1000000;//number of 20 voucher
        nbth = 1000000;//number of 30 voucher
        nbf = 3000000;//number of 50 voucher
        H = 43239;//number of customer in group A
        L = 35664;//number of customer in group B
        theta1 = -0.15;//voucher coefficients of group A
        theta2 = -0.23;//voucher coefficients of group B
        a = 2;//weight of voucher 30
        b = 3;//weight of voucher 50
}

int
main(int, char**)
{
        IloEnv env;
        try {



                define_data(env);

                IloModel model(env);
                //number variables of different voucher in differnet group
                 IloNumVar x(env, 0.0, nbtw, ILOINT);//20 in A
                 IloNumVar y(env, 0.0, nbth, ILOINT);//30 in A
                 IloNumVar z(env, 0.0, nbf, ILOINT);//50 in A
                 IloNumVar m(env, 0.0, nbtw, ILOINT);//20 in B
                 IloNumVar n(env, 0.0, nbth, ILOINT);//30 in B
                 IloNumVar l(env, 0.0, nbf, ILOINT);//50 in B

                 IloExpr Prob;
                 Prob = theta1*(x + a * y + b * z) + theta2*(m + a * n + b * l);//sum of probability in group A and B
                // Objective Function: Minimize negative probability
                model.add(IloMinimize(env, Prob));
                 //constraints
                model.add(x + y + z==H);//number of people in group A
                model.add(m + n + l == L);//..B
                model.add(x + m <= nbtw);//number of voucher 20
                model.add(y + n <= nbth);//..30
                model.add(z + l <= nbf);//..50







                // Optimize
                IloCplex cplex(model);
                cplex.setOut(env.getNullStream());
                cplex.setWarning(env.getNullStream());
                cplex.solve();
                if (cplex.getStatus() == IloAlgorithm::Infeasible)
                        env.out() << "No Solution" << endl;

                env.out() << "Solution status: " << cplex.getStatus() << endl;

                // Print results
                env.out() << "x:" << cplex.getValue(x) << endl;
                env.out() << "y:" << cplex.getValue(y) << endl;
                env.out() << "z:" << cplex.getValue(z) << endl;
                env.out() << "m:" << cplex.getValue(m) << endl;
                env.out() << "n:" << cplex.getValue(n) << endl;
                env.out() << "l:" << cplex.getValue(l) << endl;
        }
        catch (IloException& ex) {
                cerr << "Error: " << ex << endl;
        }
        catch (...) {
                cerr << "Error" << endl;
        }
        env.end();
        return 0;
}
