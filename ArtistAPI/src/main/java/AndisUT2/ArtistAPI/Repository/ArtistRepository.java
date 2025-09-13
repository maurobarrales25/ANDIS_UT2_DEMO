package AndisUT2.ArtistAPI.Repository;

import AndisUT2.ArtistAPI.Model.Artist;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class ArtistRepository {

    private final JdbcTemplate jdbcTemplate;

    private static final RowMapper<Artist> artistRowMapper = (rs, rowNum) -> {
        Artist artist = new Artist();
        artist.setArtistID(rs.getInt("artist_id"));
        artist.setName(rs.getString("name"));
        artist.setGenre(rs.getString("genre"));
        return artist;
    };

    public ArtistRepository(JdbcTemplate jdbcTemplate) {this.jdbcTemplate = jdbcTemplate;}

    public Artist getArtistByName(String name) {
        String sql = "select * from artist where name = ?";
        try {
            return jdbcTemplate.queryForObject(sql, artistRowMapper, name);
        }
        catch (EmptyResultDataAccessException e) {
            throw new RuntimeException("No se  encontro Artista con nombre: " + name);
        }
    }

    public Artist getArtistById(int artistID) {
        String sql = "select * from artist where artist_id = ?";
        try{
            return jdbcTemplate.queryForObject(sql, artistRowMapper, artistID);
        }
        catch(EmptyResultDataAccessException e){
            throw new RuntimeException("No se  encontro Artista con Id: " + artistID);
        }
    }

    public List<Artist> getAllArtists() {
        String sql = "select * from artist";
        return jdbcTemplate.query(sql, artistRowMapper);
    }

    public List<Artist> getArtistsByGenre(String genre) {
        String sql = "select * from artist where genre = ?";
        return jdbcTemplate.query(sql, artistRowMapper, genre);
    }


    public Artist saveArtist(Artist artist) {
        String sql = "insert into artist (name, genre) values (?, ?)";
        jdbcTemplate.update(sql, artist.getName(), artist.getGenre());
        return getArtistByName(artist.getName());
    }
}
