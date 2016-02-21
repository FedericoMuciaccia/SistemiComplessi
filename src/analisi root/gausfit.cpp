void fittamitutto(const char* inputdati, const char* inputparametri, const char* output)	//macro uguale alla precedente ma che popola da file un solo array di dati
{
	vector<double> ordinate;
	double appoggio;
	int i;
//////////////////////////////////////////////////////////////////
// Acquisizione dati
/////////////////////////////////////////////////////////////////
	
	bool letturaeseguita = false; //lettura del file
	do
	{
		cout << endl <<"Lettura txt di dati" << endl;		
		ifstream dati_in; //apro stream input
		dati_in.open (inputdati, ios::in);
		if (dati_in)
		{
			while(!dati_in.eof()) //popolo dinamicamente i vettori fino a che raggiunge fine del file
			{
				dati_in >> appoggio;
				ordinate.push_back(appoggio);
			}

			cout << endl << "il tuo x vettore ha " << ordinate.size() << " elementi" << endl; //TODO un bug fa popolare un elemento in più ai vettori
			cout << "Lettura del file eseguita! " << endl << endl;
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
	
	TH1F* istogramma = new TH1F("istogramma","title",ordinate.size(),0,ordinate.size()); //definisci istogrammi
	for(i = 0; i < ordinate.size()-1; i++)
		istogramma->SetBinContent(i,ordinate[i]);
	
	TCanvas *oggetto = new TCanvas(); //apro "tela"
	oggetto->SetLogy();
	gStyle->SetOptStat(0);

	istogramma->SetTitle("Distribuzione del grado");
	istogramma->SetLineColor(1);
// 	istogramma->SetFillStyle();
	istogramma->GetXaxis()->SetTitle("Grado");
	istogramma->GetYaxis()->SetTitle("Conteggi");
	istogramma->SetFillColor(kYellow-8);
// 	istogramma->GetXaxis()->SetRange(6681,6780);	 //parte bassa coba
// 	istogramma->GetYaxis()->SetRangeUser(1,1000);//parte media coba
	
/////////////////////////////////////////////
// PARTE IN CUI SI FITTA TUTTO
//////////////////////////////////////////////
	double piatto; 
	double massimo;
	double binmedio;
	double sigma;
	double bmin;
	double bmax;
	double chi2;
	int ndati = 0;
	int primo;

//////////////////////////////////////////////////////////////////
// Acquisizione dati
/////////////////////////////////////////////////////////////////
	
	bool letturaeseguita = false; //lettura del file
	do
	{
		cout << endl <<"Lettura txt di dati" << endl;
		
		ifstream dati_in; //apro stream input
		dati_in.open (inputparametri, ios::in);
		if (dati_in)
		{
			i = 0;
			while(!dati_in.eof()) //popolo dinamicamente i vettori fino a che raggiunge fine del file
			{
				dati_in >> piatto;
				dati_in >> massimo;
				dati_in >> binmedio;
				dati_in >> sigma;
				dati_in >> bmin;
				dati_in >> bmax;

				i++;
			}
			cout << "Lettura del file eseguita! " << endl << endl;
			letturaeseguita = true;
		}
		else
		{
			cout << "Impossibile leggere il file " << endl;
			letturaeseguita = false;
		}
		dati_in.close();
	} while(!letturaeseguita);
	
	double exp[20];
	bool scritturaeseguita = false;
	do
	{
		//creazione di uno stream e sua associazione al file (apertura e successiva chiusura)
		ofstream file_out;
		file_out.open (output, ios::app);//è meglio specificare la modalità (ios::out sovrascrive, ios::app no)
		if (file_out)
		{
			file_out << "binmedio err sigma errsigma\t\tchirid" << endl;
			//fit con nonpiatto
			TF1 *picco = new TF1("picco", "[0]+gaus(1)", bmin, bmax);	// definisco funzione di fitting: retta (background) + gaussiana (segnale)
			picco->SetParameters(piatto,massimo,binmedio,sigma); 	//setto i parametri definiti in precedenza
			picco->SetLineWidth(3);
			istogramma->Fit("picco", "MR+","SAME");	//fa il fit, restituisce parametri finali e traccia istogramma (se converge)
						
			chi2 = picco -> GetChisquare();
			piatto = picco -> GetParameter(0);
			massimo = picco -> GetParameter(1);
			binmedio = picco -> GetParameter(2);
			errbinmedio = picco -> GetParError(2);
			sigma = picco -> GetParameter(3);
			errsigma = picco -> GetParError(3);
			file_out  << binmedio << " " << errbinmedio << " " << sigma << " " << errsigma;
			//scrittura sul file
			file_out << "\t\t" << chi2/(bmax-bmin-4) << "  s/r  "<< massimo/piatto <<  endl;
			file_out << bmax-bmin-4 << " " << chi2 << " " << endl << endl;
		}
		else
		{
			cout << "Impossibile aprire/creare il file " << endl;
			scritturaeseguita = false;
		}
		//chiusura del file (è importante che il file venga sempre chiuso)
		file_out.close();
	}while (!scritturaeseguita);
	
	TCanvas *oggetto2 = new TCanvas(); //apro "tela"
	oggetto2->SetLogy();
	gStyle->SetOptStat(0);
	
	TH1F* calibrato = new TH1F("istogramma","title",ordinate.size(),0,ordinate.size()); //definisci istogrammi
	for(i=0; i < ordinate.size(); i++)
		calibrato->SetBinContent(i,ordinate);
	
	
// 	calibrato->SetTitle("Spettro con fit in keV");
// 	calibrato->SetTitle("Spettro con fit in keV: parte alta");
	calibrato->SetTitle(" ");
// 	calibrato->SetTitle("Spettro con fit in keV: parte bassa");
	calibrato->SetLineColor(1);
// 	calibrato->SetFillStyle();
	calibrato->GetXaxis()->SetTitle("Energia (keV)");
	calibrato->GetYaxis()->SetTitle("Conteggi");
	calibrato->SetFillColor(kYellow-8);

// 	calibrato->GetXaxis()->SetRange(0,401/m); //tutto coba
// 	calibrato->GetXaxis()->SetRange(260/m,401/m);	 //parte alta coba
// 	calibrato->GetXaxis()->SetRange(190,1600); //parte bassa coba
// 	calibrato->GetXaxis()->SetRange(0,402); //parte media coba
	
// 	calibrato->GetYaxis()->SetRangeUser(1,100000);
	calibrato->GetYaxis()->SetTitleOffset(0.5);	
// 	calibrato->GetXaxis()->SetNdivisions(5,5,0,kTRUE);
	calibrato->Draw("");
	
	

	TF1 *piccoE = new TF1("picco", "[0]+gaus(1)", bmin, bmax);	// definisco funzione di fitting: retta (background) + gaussiana (segnale)
	piccoE->SetParameters(piatto,massimo,binmedio,sigma); 	//setto i parametri definiti in precedenza
	piccoE->SetLineWidth(3);
	piccoE->Draw("SAME");



	legenda = new TLegend(0.897,0.895,0.698,0.795);
	legenda->SetFillColor(0);
	legenda->AddEntry(istogramma,"Spettro misurato","f");
	legenda->AddEntry(piccoE,"Fit ^{133}Ba","L");
	legenda->AddEntry(piccoCoE, "Fit ^{57}Co", "L");
	legenda->Draw("SAME");
	calibrato->Draw("SAMEAXIS");	
	cout << "Scrittura su file eseguita! " << endl << endl;
}
