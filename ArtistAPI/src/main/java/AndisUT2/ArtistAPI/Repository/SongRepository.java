package AndisUT2.ArtistAPI.Repository;

import AndisUT2.ArtistAPI.Model.Song;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class SongRepository {

    private final JdbcTemplate jdbcTemplate;

    public SongRepository(JdbcTemplate jdbcTemplate) {this.jdbcTemplate = jdbcTemplate;}

    private  static final RowMapper<Song> songMapper = (rs, rowNum) -> {
        Song song = new Song();
        song.setSongID(rs.getInt("song_id"));
        song.setSongName(rs.getString("song_name"));
        song.setArtistID(rs.getInt("artist_id"));
        song.setAlbumID(rs.getInt("album_id"));
        return song;
    };

    public Song getSongByID(int songID) {
        String sql = "select * from song where songID=?";
        try {
            return jdbcTemplate.queryForObject(sql, songMapper, songID);
        }
        catch (EmptyResultDataAccessException e) {
            throw new RuntimeException("No se encontro cancion con ID: " + songID);
        }
    };

    public List<Song> getAllSongs() {
        String sql = "select * from song";
        return jdbcTemplate.query(sql, songMapper);
    }

    public Song getSongByName(String songName) {
        String sql = "select * from song where songName=?";
        try{
            return jdbcTemplate.queryForObject(sql, songMapper, songName);
        }
        catch (EmptyResultDataAccessException e) {
            throw new RuntimeException("No se encontro cancion con ID: " + songName);
        }
    }

    public List<Song> getSongsByArtistID(int artistID) {
        String sql = "select * from song where artistID=?";
        return jdbcTemplate.query(sql, songMapper, artistID);
    }

    public List<Song> getSongsByAlbumID(int albumID) {
        String sql = "select * from song where albumID=?";
        return jdbcTemplate.query(sql, songMapper, albumID);
    }
}
