package AndisUT2.ArtistAPI.Model;



public class Album {

    private int albumId;
    private String albumName;
    private int artistId;

    public Album(int albumId, String albumName, int artistId) {
        this.albumId = albumId;
        this.albumName = albumName;
        this.artistId = artistId;
    }

    public Album(String albumName, int artistId) {
        this.albumName = albumName;
        this.artistId = artistId;
    }

    public Album(){}

    public int getAlbumId() {
        return albumId;
    }

    public void setAlbumId(int albumId) {
        this.albumId = albumId;
    }

    public String getAlbumName() {
        return albumName;
    }

    public void setAlbumName(String albumName) {
        this.albumName = albumName;
    }

    public int getArtistId() {
        return artistId;
    }

    public void setArtistId(int artistId) {
        this.artistId = artistId;
    }
}
