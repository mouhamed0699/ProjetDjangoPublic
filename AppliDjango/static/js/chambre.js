
function validateSelection() {
  var select1 = document.getElementById("select1");
  var select2 = document.getElementById("select2");
  console.log(select1.value)

  if (select1.value !== "") {
    select2.disabled = false;
  } else {
    select2.disabled = true;
  }
}

validateSelection()


var select1 = document.getElementById("select1");

hotel_Dakar=['LODGE DU DELTA NIOMINKA-ILE DE DIONEWAR','HOTEL DU PHARE LES MAMELLES - GUESTHOUSE','TERROU-BI HOTEL CASINO MARINA',
'RADISSON BLU DAKAR','HOTEL LA VILLA RACINE','THE RHINO HOTEL RESORT & SPA','HOTEL JARDIN SAVANA DAKAR']

hotel_Paris=['MAYET','TRINITE PLAZA','BOULOGNE RESIDENCE HOTEL','HOTEL RESIDENCE EUROPE','RESIDENCE CERISE MAISONS LAFFITTE','HOTEL DU CHATEAU',
'LE NOTRE DAME','ETOILE PARK HOTEL','ALEXANDRINE OPERA','DU CADRAN']

select1.addEventListener('change', () => {
    const newOption = select1.options[select1.selectedIndex].value;
    var select2 = document.getElementById("select2");
    select2.innerHTML = ""
    if (newOption === 'Dakar') {
      hotel_Dakar.forEach(hotel => {
        const option1 = document.createElement('option');
        option1.value = hotel;
        option1.textContent = hotel;
        select2.appendChild(option1);
      });
    } else {
      hotel_Paris.forEach(hotel => {
        const option1 = document.createElement('option');
        option1.value = hotel;
        option1.textContent = hotel;
        select2.appendChild(option1);
      });
    }
  });
  


