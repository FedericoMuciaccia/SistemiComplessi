
void graficifit(const char* input)	//macro uguale alla precedente ma che popola da file un solo array di dati
{
	double appoggio;
	vector<double> ascisse;
	vector<double> ordinate;
	int i;
	
//////////////////////////////////////////////////////////////////
// Acquisizione dati
/////////////////////////////////////////////////////////////////
	
	bool letturaeseguita = false; //lettura del file
	do
	{

		cout << endl <<"Lettura txt di dati" << endl;
		
		ifstream dati_in; //apro stream input
		dati_in.open (input, ios::in);
		
		if (dati_in)
		{
			i=0;
			while(!dati_in.eof()) //popolo dinamicamente i vettori fino a che raggiunge fine del file
			{
				ascisse.push_back(i);
				i++;

				dati_in >> appoggio;		//popolo il vettore delle energie nominali (no error)
				ordinate.push_back(appoggio);
			}
			
			cout << "Lettura del file eseguita! " << endl << endl;
			letturaeseguita = true;
		}
		else
		{
			cout << "Impossibile leggere il file " << endl;
			cout << "controllare se il percorso inserito è corretto " << endl;
			letturaeseguita = false;
		}
		dati_in.close();
	} while(!letturaeseguita);
	
//////////////////////////////////////////////////////////////////////////
// Parte di programma in cui si usa root
//////////////////////////////////////////////////////////////////////////
	
	for(i=1; i<ascisse.size(); i++)
	{
// 		cout << ascisse[i] << " " << ordinate[i] << endl;
		ascisse[i] = log(ascisse[i]);
		if(ordinate[i] > 0)
			ordinate[i] = log(ordinate[i]);
// 		cout << ascisse[i] << " " << ordinate[i] << endl;
	}
	double prova;
	prova = log(2.7);
	cout << prova << endl;
	vector<double> parametri;
	double chi2;
	
	appoggio = 20;
	parametri.push_back(appoggio);
	parametri.push_back(-3);
	
	TCanvas *oggetto = new TCanvas(); //apro "tela"
	//TGraph *grafico = new TGraph(x.size(),ascisse,ordinate);  //grafico senza errori
	TGraph *grafico = new TGraph(ascisse.size(), &ascisse[0], &ordinate[0]); //grafico con errori
// 	TAxis *axis = grafico->GetXaxis();
		
	grafico->SetMarkerColor(2); //impostazioni stilistiche del grafico
	grafico->SetMarkerStyle(20);
	grafico->SetMarkerSize(0.5);
	
	grafico->SetTitle("Calibrazione ^{133}Ba");
	grafico->GetXaxis()->SetTitle("Posizione (bin)");
	grafico->GetYaxis()->SetTitle("Energia (keV)");
// 	grafico->GetYaxis()->SetNdivisions(5,5,0,kTRUE);
	
// 	axis->SetLimits(0,7000);
// 	grafico->GetHistogram()->SetMaximum(400);         
// 	grafico->GetHistogram()->SetMinimum(0);
	
 	grafico->Draw("AP"); // traccia il grafico dei punti

	TF1 *retta = new TF1("retta", "[0]+[1]*x", 4.9, 5.8);	// definisco funzione di fitting: retta
 	retta->SetParameters(parametri[0], parametri[1]); 	//setto i parametri definiti in precedenza
 	retta->SetLineColor(kBlue+2);
	retta->SetLineWidth(1);
			
	grafico->Fit("retta", "R");	//fa il fit (minimi chi^2), dà parametri finali e traccia grafico (se converge)
}
