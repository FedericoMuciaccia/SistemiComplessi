
void spettramitutto(const char* inputdati)	//macro uguale alla precedente ma che popola da file un solo array di dati
{
	vector<double> ordinate;
	double appoggio;
	double shaping;
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
// 			dati_in >> shaping;
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
	
	TH1F* istogramma = new TH1F("istogramma","title",ordinate.size(),0,ordinate.size());
	
	shaping = ordinate[0];
	for(i = 1; i < ordinate.size()-1; i++) 
		istogramma->SetBinContent(i,ordinate[i]);
	
	TCanvas *oggetto = new TCanvas(); //apro "tela"
	oggetto->SetLogy();
	oggetto->SetLogx();
	gStyle->SetOptStat(0);
	
	istogramma->SetTitle("Distribuzione del grado");
//	istogramma->GetXaxis()->SetRangeUser(4975,5175);
// 	istogramma->GetYaxis()->SetRangeUser(1,10001);
	
	istogramma->SetLineColor(1);
	istogramma->GetXaxis()->SetTitle("Grado");
	istogramma->GetYaxis()->SetTitle("Conteggi");
	istogramma->SetFillColor(kYellow-8);
	istogramma->GetXaxis()->SetNdivisions(5,5,0,kTRUE);
	// 	istogramma->GetYaxis()->SetTitleOffset(1.5);
	istogramma->Draw();
	
	legenda = new TLegend(0.897,0.895,0.698,0.835);
	legenda->SetFillColor(0);
	if(ordinate[0]==0)
		legenda->AddEntry(istogramma,"Dati aggregati","f");
	if(ordinate[0]==1)
		legenda->AddEntry(istogramma,"Tim","f");
	if(ordinate[0]==2)
		legenda->AddEntry(istogramma,"Voda","f");
	if(ordinate[0]==3)
		legenda->AddEntry(istogramma,"Wind","f");
	if(ordinate[0]==4)
		legenda->AddEntry(istogramma,"Tre","f");

	legenda->Draw("SAME");
	istogramma->Draw("SAMEAXIS");
}


void spettral()
{
	spettramitutto("IstoGrado_Roma");
	spettramitutto("IstoGrado_Tim");
	spettramitutto("IstoGrado_Voda");
	spettramitutto("IstoGrado_Wind");
	spettramitutto("IstoGrado_Tre");
}