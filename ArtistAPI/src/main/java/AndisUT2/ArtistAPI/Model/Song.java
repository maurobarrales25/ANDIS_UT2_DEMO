package AndisUT2.ArtistAPI.Model;

public class Song {

    private int songID;
    private String songName;
    private int artistID;
    private int albumID;

    public Song(int songID, String songName, int artistID, int albumID) {
        this.songID = songID;
        this.songName = songName;
        this.artistID = artistID;
        this.albumID = albumID;
    }

    public Song(){}

    public int getSongID() {
        return songID;
    }

    public void setSongID(int songID) {
        this.songID = songID;
    }

    public String getSongName() {
        return songName;
    }

    public void setSongName(String songName) {
        this.songName = songName;
    }

    public int getArtistID() {
        return artistID;
    }

    public void setArtistID(int artistID) {
        this.artistID = artistID;
    }

    public int getAlbumID() {
        return albumID;
    }

    public void setAlbumID(int albumID) {
        this.albumID = albumID;
    }
}
