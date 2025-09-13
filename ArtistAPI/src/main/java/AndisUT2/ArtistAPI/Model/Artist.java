package AndisUT2.ArtistAPI.Model;

public class Artist {

    private int artistID;
    private String name;
    private String genre;

    public Artist(int artistID, String name, String genre) {
        this.artistID = artistID;
        this.name = name;
        this.genre = genre;
    }

    public Artist(String name, String genre) {
        this.name = name;
        this.genre = genre;
    }

    public Artist(String name){
        this.name = name;
    }

    public Artist() {}

    public int getArtistID() {
        return artistID;
    }

    public void setArtistID(int artistID) {
        this.artistID = artistID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }
}
