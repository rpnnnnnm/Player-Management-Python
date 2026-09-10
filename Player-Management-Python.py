Program Management_Player_Game 
{Program untuk mengelola data pemain menggunakan struktur array of record, 
mencakup fitur input, tampil data, pengurutan level secara descending, dan 
pencarian nickname} 
 
{I.S. : Sistem siap dijalankan, memori untuk array players telah dialokasikan 
(kosong atau berisi data)} 
{F.S. : Seluruh instruksi manajemen data selesai dieksekusi dan program 
berhenti saat pengguna memilih menu keluar} 
 
Deklarasi: 
    {Definisi Struktur Data} 
    type PlayerRecord : <nickname : string, level : integer, inventory : 
array of string> 
     
    {Variabel Global / Utama} 
    players : array [1..100] of PlayerRecord 
    daftar_item : array [1..9] of string = ["Potion Heal", "Dagger", "Iron 
Sword", "Shield", "Bow", "Arrow", "Helmet", "Armor", "Mana potion"] 
     
    {Variabel Pendukung Seluruh Modul} 
    pilih, posisi, n, i, j : integer 
    nickname_cari, n_nickname : string 
    n_level, n_jumlah, n_pilih : integer 
    n_inventory : array of string 
    m : PlayerRecord 
    ketemu : boolean 
 
Algoritma: 
    {------------------------------------------------------------------} 
    { 1. ALGORITMA UTAMA                                               } 
    {------------------------------------------------------------------} 
    repeat 
        output("==============================") 
        output("MENU MANAGEMENT PLAYER GAME") 
        output("==============================") 
        output("1. Input Data Player") 
        output("2. Tampil Data Player") 
        output("3. Urutkan Data Player (Level)") 
        output("4. Cari Data Player (Nickname)") 
        output("5. Keluar") 
        output("Pilih menu: ") 
        input(pilih) 
 
        depend on pilih 
            1 : call inputData(players) 
            2 : call tampilData(players) 
            3 : call insertionTurun(players, length(players)) 
                output("Data berhasil diurutkan berdasarkan level tertinggi.") 
            4 : output("Masukkan nickname yang dicari: ") 
                input(nickname_cari) 
 

 
                posisi <- call sequential_search(players, nickname_cari) 
                if (posisi != -1) then 
                    output("Data ditemukan pada indeks: ", posisi + 1) 
                    output("Nickname: ", players[posisi].nickname) 
                    output("Level: ", players[posisi].level) 
                else 
                    output("Data player tidak ditemukan.") 
                endif 
            5 : output("Keluar dari program.") 
        enddepend 
    until (pilih = 5) 
 
    {------------------------------------------------------------------} 
    { 2. PROSEDUR inputData                                            } 
    {------------------------------------------------------------------} 
    Procedure inputData(input/output data : array of PlayerRecord) 
    begin 
        output("Masukkan nickname: ") 
        input(n_nickname) 
        output("Masukkan level: ") 
        input(n_level) 
        output("Jumlah item: ") 
        input(n_jumlah) 
 
        output("DAFTAR ITEM:") 
        for i <- 0 to length(daftar_item) - 1 do 
            output(i + 1, ". ", daftar_item[i]) 
        endfor 
 
        for i <- 1 to n_jumlah do 
            output("Pilih nomor item: ") 
            input(n_pilih) 
            n_inventory[i] <- daftar_item[n_pilih - 1] 
        endfor 
 
        data[length(data) + 1] <- [n_nickname, n_level, n_inventory] 
        output("Data Berhasil Disimpan.") 
    endprocedure 
 
    {------------------------------------------------------------------} 
    { 3. PROSEDUR tampilData                                           } 
    {------------------------------------------------------------------} 
    Procedure tampilData(input data : array of PlayerRecord) 
    begin 
        if (length(data) = 0) then 
            output("Data player kosong.") 
        else 
            output("=== DATA PLAYER ===") 
            for i <- 0 to length(data) - 1 do 
                output("Player ke-", i + 1) 
                output("Nickname: ", data[i].nickname) 
                output("Level: ", data[i].level) 
                output("Inventory: ") 
                for j <- 0 to length(data[i].inventory) - 1 do 
                    output(" - ", data[i].inventory[j]) 
                endfor 
            endfor 
        endif 
    endprocedure 

    {------------------------------------------------------------------} 
    { 4. PROSEDUR insertionTurun                                       } 
    {------------------------------------------------------------------} 
    Procedure insertionTurun(input/output data : array of PlayerRecord, input 
n : integer) 
    begin 
        for i <- 1 to n - 1 do 
            m <- data[i] 
            j <- i - 1 
            ketemu <- false 
            while (j >= 0 and not ketemu) do 
                if (m.level > data[j].level) then 
                    data[j + 1] <- data[j] 
                    j <- j - 1 
                else 
                    ketemu <- true 
                endif 
            endwhile 
            data[j + 1] <- m 
        endfor 
    endprocedure 
 
    {------------------------------------------------------------------} 
    { 5. FUNGSI sequential_search                                      } 
    {------------------------------------------------------------------} 
    Function sequential_search(input data : array of PlayerRecord, input 
dicari : string) -> integer 
    begin 
        i <- 0 
        while (i < length(data) and data[i].nickname != dicari) do 
            i <- i + 1 
        endwhile 
 
        if (i < length(data)) then 
            return i 
        else 
            return -1 
        endif 
    endfunction 