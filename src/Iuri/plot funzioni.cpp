
void graficifit(const char* input)	//macro uguale alla precedente ma che popola da file un solo array di dati
{
	double appoggio;
	vector<double> ascisse;
	vector<double> ordinate;
	
//////////////////////////////////////////////////////////////////
// Acquisizione dati
/////////////////////////////////////////////////////////////////
	
	bool letturaeseguita = false; //lettura del file
	do
	{
		ifstream dati_in; //apro stream input
		dati_in.open (input, ios::in);
		
		if (dati_in)
		{
			while(!dati_in.eof()) //popolo dinamicamente i vettori fino a che raggiunge fine del file
			{
				dati_in >> appoggio;		//popolo vettore delle ascisse (bin del picco medio)
				ascisse.push_back(appoggio);
				
				dati_in >> appoggio;		//popolo il vettore delle energie nominali (no error)
				ordinate.push_back(appoggio);
			}
			letturaeseguita = true;
		}
		else
		{
			cout << "Impossibile leggere il file " << endl;
			letturaeseguita = false;
		}
		dati_in.close();
	} while(!letturaeseguita);
	
//////////////////////////////////////////////////////////////////////////
// Parte di programma in cui si usa root
//////////////////////////////////////////////////////////////////////////
	
	
	TCanvas *oggetto = new TCanvas(); //apro "tela"
	TGraph *grafico = new TGraph(ascisse.size(), &ascisse[0], &ordinate[0]);
	TAxis *axis = grafico->GetXaxis();
		
	grafico->SetMarkerColor(1); //impostazioni stilistiche del grafico
	grafico->SetMarkerStyle(20);
	grafico->SetMarkerSize(0.9);
	
	grafico->SetTitle("Confronto C(p)");
	grafico->GetXaxis()->SetTitle("p");
	grafico->GetYaxis()->SetTitle("C");
	grafico->GetYaxis()->SetNdivisions(10,3,0,kTRUE);
	grafico->GetXaxis()->SetNdivisions(10,3,0,kTRUE);
	
	axis->SetLimits(0,1.05);
	grafico->GetHistogram()->SetMaximum(0.80);         
	grafico->GetHistogram()->SetMinimum(0);
	
 	grafico->Draw("AP"); // traccia il grafico dei punti

	TF1 *retta = new TF1("retta", "x", -0.1, 1);	// definisco funzione di fitting: retta
	retta->SetLineColor(kGreen-6);
	retta->SetLineWidth(3);
	retta->Draw("SAME");
	
	TF1 *curva = new TF1("curva", "0.75*(1-x)**3", -0.1, 1);	// definisco funzione di fitting: retta
	curva->SetLineColor(kBlue-7);
	curva->SetLineWidth(3);
	curva->Draw("SAME");
	
	grafico->Draw("PSAME");		
	
	legenda = new TLegend(0.957,0.955,0.785,0.825);
	legenda->SetFillColor(0);
	legenda->AddEntry(retta,"C_{ER}(p)","L");
 	legenda->AddEntry(curva, "C_{WS}(p)", "L");
	legenda->Draw("SAME");
}